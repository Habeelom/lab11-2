from typing import Dict
from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    """
    Anonymizes text by replacing it with initials.
    """

    def operate(self, text: str = None, params: Dict = None) -> str:
        if not text:
            return ""
        
        # split() without arguments automatically handles multiple spaces
        words = text.split()
        
        # Take first char, uppercase it, add dot
        initials = [f"{word[0].upper()}." for word in words]
        
        return " ".join(initials)

    def validate(self, params: Dict = None) -> None:
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize