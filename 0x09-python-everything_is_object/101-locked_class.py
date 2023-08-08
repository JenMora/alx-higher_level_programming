#!/usr/bin/python3
class LockedClass:
    """
    A class that prevents the user from dynamically
    creating new instance attributes,
    except if the new instance attribute is called 'first_name'.
    """

    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        """
        Override the default attribute setting behavior.

        Args:
            name (str): The name of the attribute.
            value: The value to set for the attribute.

        Raises:
            AttributeError: If the attribute is not
            'first_name' and doesn't already exist.
        """
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError(f"'LockedClass' object has\
                    no attribute '{name}'")
        super().__setattr__(name, value)
