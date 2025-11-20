import re # <--- Don't forget this import at the top!
from typing import Dict
from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    def operate(self, text: str = None, params: Dict = None) -> str:
        if not text:
            return ""
        
        words = text.split()
        initials = []
        
        for word in words:
            # Find prefix (non-word chars) and the first word char
            match = re.search(r'^(\W*)(\w)', word)
            if match:
                prefix = match.group(1)
                char = match.group(2).upper()
                initials.append(f"{prefix}{char}.")
            else:
                # Fallback if no word characters are found
                initials.append(word)

        return " ".join(initials)

    def validate(self, params: Dict = None) -> None:
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize