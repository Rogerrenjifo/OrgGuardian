from abc import ABC, abstractmethod


class Analyzable(ABC):
    """
    An abstract class that defines methods that should be implemented by subclasses.
    Subclasses must implement the `analyze` method to process information.

    Methods:
        analyze(image): Process the provided information.

    Args:
        image: The information to be analyzed.

    Raises:
        NotImplementedError: This method must be implemented by subclasses.
    """

    @abstractmethod
    def analyze(self, image):
        """
        Process the provided information.
        Analyze the image and return the results i
        Args:
            image: The information to be analyzed.

        Returns:
            None

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
