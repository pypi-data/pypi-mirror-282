import os
import typing as T
from abc import abstractmethod
from dataclasses import dataclass

from .ingredient_category import Category

no_default = object()

@dataclass
class IODefinition:
    """Defines a IO of a ingredient."""

    #: label to be show on the UI
    label: T.Optional[str] = None
    #: value of the IO
    value: T.Any = None
    #: translated label to be show on the UI. Must be Non if is_editable is True
    label_translated: T.Optional[T.Dict[str, str]] = None
    #: additional arguments to be passed to the ingredient
    argname: T.Optional[str] = None
    #: type of data that can be passed to the IO
    type: T.Any = T.Any

    def get_translated_label(self, language=None):
        assert not (
            self.label_translated is not None and self.is_editable
        ), "Editable IOs cannot have translated labels"
        if self.label_translated is not None:
            if language is None:
                language = os.getenv("LANGUAGE", "en")
            return self.label_translated.get(language, self.label)
        return self.label

@dataclass
class Parameter:
    """Defines a parameter of a ingredient."""

    #: name of the parameter
    name: T.Optional[str] = None
    #: value of the parameter
    value: T.Any = None
    #: type of data that can be passed to the parameter
    type: T.Any = T.Any
    #: default value of the parameter
    default: T.Any = no_default
    
    def has_default_value(self):
        return self.default is not no_default
    
    @property
    def default_value(self):
        if self.has_default_value():
            return self.default
        raise ValueError("No default value set for parameter")
    
    def _reset_to_default(self):
        if self.has_default_value():
            self.value = self.default_value
        else:
            raise ValueError("No default value set for parameter")


class Pinch(IODefinition):
    """Defines a pinch port.
    
    Pinch port is the input port that is used to connect to the output port of another ingredient.
    """

    def __init__(self, **kwargs):
        super().__init__()
        self.is_input: bool = True
        #: whether the parameter is required
        self.required: bool = True
        #: default value of the parameter
        self.default: T.Any = no_default
        for key, value in kwargs.items():
            setattr(self, key, value)

    def has_default_value(self):
        return self.default is not no_default

    @property
    def default_value(self):
        if self.has_default_value():
            return self.default
        raise ValueError("No default value set for parameter")

    def _reset_to_default(self):
        if self.has_default_value():
            self.value = self.default_value
        else:
            raise ValueError("No default value set for parameter")

class Taste(IODefinition):
    """Defines a taste port.
    
    Taste port is the output port that is used to connect to the input port of another ingredient.
    """

    def __init__(self, **kwargs):
        super().__init__()
        self.is_output = True
        for key, value in kwargs.items():
            setattr(self, key, value)


class BaseIngredient:
    """Base class for all ingredients."""
    
    category = Category.HIDDEN
    outputs = []

    def __init__(self):
        #: name of the ingredient
        self.name: T.Optional[str] = None
        #: description of the ingredient
        self.description: T.Optional[str] = None
        #: author of the ingredient (TODO: should be a User object or something similar)
        self.author: T.Optional[str] = None
        #: version of the ingredient
        self.version: T.Optional[str] = None
        #: platform of the ingredient
        self.platform = "python"
        #: dependencies of the ingredient, can be loaded from requirements.txt
        self.dependencies: T.List[str] = []
        #: IO of the ingredient
        self.key_list: T.List[str] = []
        self.pinches: T.Dict[str, Pinch] = {}
        self.tastes: T.Dict[str, Taste] = {}
        #: parameters to configure the ingredient
        self.parameters: T.Dict[str, Parameter] = {}
    
    def __validate_key(self, key: str):
        """Validate the key for the ingredient.
        Key must be a valid identifier and must not be already defined.
        """
        if not key.isidentifier():
            raise ValueError("Key must be a valid identifier")
        if key in self.key_list:
            raise ValueError(f"Key {key} already defined")
        self.key_list.append(key)

    def add_parameter(self, name, type, default=no_default):
        self.__validate_key(name)
        self.parameters[name] = Parameter(name=name, type=type, default=default)
        
    def get_parameter(self, name):
        return self.parameters[name].value
    
    def set_parameter(self, name, value):
        if name not in self.parameters.keys():
            raise ValueError(f"Parameter {name} not found in {self.name}")
        assert value is None or isinstance(value, self.parameters[name].type), f"Value {value} is not of type {self.parameters[name].type}"
        self.parameters[name].value = value
    
    def add_pinch(self, label, type, **kwargs):
        self.__validate_key(label)
        self.pinches[label] = Pinch(label=label, type=type, **kwargs)
    
    def get_pinch(self, label):
        return self.pinches[label].value
    
    def set_pinch(self, label, value):
        if label not in self.pinches.keys():
            raise ValueError(f"Pinch {label} not found in {self.name}")
        assert value is None or isinstance(value, self.pinches[label].type), f"Value {value} is not of type {self.pinches[label].type}"
        self.pinches[label].value = value
    
    def add_taste(self, label, type, **kwargs):
        self.__validate_key(label)
        self.tastes[label] = Taste(label=label, type=type, **kwargs)
    
    def get_taste(self, label):
        return self.tastes[label].value
    
    def set_taste(self, label, value):
        if label not in self.tastes.keys():
            raise ValueError(f"Taste {label} not found in {self.name}")
        assert value is None or isinstance(value, self.tastes[label].type), f"Value {value} is not of type {self.tastes[label].type}"
        self.tastes[label].value = value

    def _reset_to_default(self):
        """Reset all parameters and pinches to their default values."""
        for parameter in self.parameters.values():
            parameter._reset_to_default()
        for pinch in self.pinches:
            pinch._reset_to_default()
    
    def __make_io(self, *args, **kwargs):
        """Set the values of pinches and parameters using the given arguments."""
        args_ext = []
        kwargs_ext = {}
        # set values for pinches when using keyword arguments
        for key, value in kwargs.items():
            if key in self.pinches:
                self.pinches[key].value = value
            elif key in self.parameters:
                self.parameters[key].value = value
            else:
                # add a new pinch if no key is found
                kwargs_ext[key] = value
                self.add_pinch(key, type(value), value=value)
        
        # set values for pinches when using positional arguments
        for value in args:
            found = False
            for key, pinch in self.pinches.items():
                if pinch.value is None:
                    pinch.value = value
                    found = True
                    break
            if not found:
                args_ext.append(value)            

        # check if all required pinches are set
        for key, pinch in self.pinches.items():
            if pinch.required and pinch.value is None:
                if pinch.has_default_value():
                    pinch.value = pinch.default_value
                else:
                    raise ValueError(f"Pinch {key} is required but not set")
        
        # check if all required parameters are set
        for key, parameter in self.parameters.items():
            if parameter.value is None:
                if parameter.has_default_value():
                    parameter.value = parameter.default_value
                else:
                    raise ValueError(f"Parameter {key} is required but not set")

        # add extend tastes when outputs are defined
        for output in self.outputs:
            if output not in self.tastes:
                self.add_taste(output, T.Any)
        
        return args_ext, kwargs_ext
    
    def __validate_output(self, *args):
        """Validate the output of the ingredient."""
        for idx in range(len(self.outputs)):
            self.tastes[self.outputs[idx]].value = args[idx]
        for key, taste in self.tastes.items():
            if taste.value is None:
                raise ValueError(f"Taste {key} is not set")
        
    def __call__(self, *args, **kwargs):
        args_ext, kwargs_ext = self.__make_io(*args, **kwargs)
        outputs = self.run(*args_ext, **kwargs_ext)
        self.__validate_output(outputs)
    
    @abstractmethod
    def run(self, *args, **kwargs):
        pass
