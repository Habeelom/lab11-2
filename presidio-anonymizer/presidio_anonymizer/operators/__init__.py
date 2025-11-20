"""Anonymizer operators."""
from .operator import Operator, OperatorType
from .hash import Hash
from .mask import Mask
from .redact import Redact
from .replace import Replace
from .custom import Custom
from .encrypt import Encrypt
from .decrypt import Decrypt
from .keep import Keep
from .deanonymize_keep import DeanonymizeKeep
from .initial import Initial  # <--- 1. Ensure this is here

# Optional dependencies
try:
    from .surrogate_ahds import AHDSSurrogate
    AHDS_AVAILABLE = True
except ImportError:
    AHDSSurrogate = None
    AHDS_AVAILABLE = False

# 2. Factory MUST be imported LAST to prevent circular errors
from .operators_factory import OperatorsFactory  # isort:skip

__all__ = [
    "Operator",
    "OperatorType",
    "Hash",
    "Mask",
    "Redact",
    "Replace",
    "Custom",
    "Encrypt",
    "Decrypt",
    "Keep",
    "DeanonymizeKeep",
    "Initial",  # <--- 3. Ensure this is in the list
    "OperatorsFactory",
    "AHDSSurrogate",
    "AHDS_AVAILABLE",
]