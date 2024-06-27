# Metaclass definition
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # Print message when creating class
        print("Creating class:", name)

        # Dictionary to hold new properties
        new_dct = {}

        # Iterate through class attributes
        for key, value in dct.items():
            # Check if the attribute is a property
            if isinstance(value, property):
                # Set __name__ and __qualname__ for existing properties
                value = cls._set_property_name(value, name, key)
                new_dct[key] = value  # Keep existing property
            else:
                # Automatically create property for attributes
                def getter(self, k=key):
                    return getattr(self, f"_{k}", None)

                def setter(self, val, k=key):
                    setattr(self, f"_{k}", val)

                # Replace attribute with property
                prop = property(getter, setter)
                prop = cls._set_property_name(prop, name, key)
                new_dct[key] = prop

        # Call the parent __new__ method to create the class
        return super().__new__(cls, name, bases, new_dct)

    @staticmethod
    def _set_property_name(prop, cls_name, attr_name):
        prop.__set_name__(cls_name, attr_name)
        return prop

# Example usage of the metaclass
class MyClass(metaclass=MyMeta):
    def __init__(self, name):
        self._name = name  # Underlying attribute

    # Attribute with automatic property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

# Creating an instance of MyClass
obj = MyClass("Alice")

# Using the property
print(obj.name)  # Output: Alice

# Setting the property
obj.name = "Bob"
print(obj.name)  # Output: Bob
