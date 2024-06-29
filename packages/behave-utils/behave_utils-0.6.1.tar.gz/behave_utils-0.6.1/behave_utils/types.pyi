#  Copyright 2024  Dominik Sekotill <dom.sekotill@kodo.org.uk>
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
General type definitions
"""

from typing import Protocol
from typing import TypeVar

S_co = TypeVar("S_co", bound=str|bytes, covariant=True)


class Readable(Protocol[S_co]):
	"""
	Protocol for types that implement the read() method of file-like objects
	"""

	def read(self, _s: int = ..., /) -> S_co: ...
