from typing import List


class AdapterBase:
    async def translate(self, texts: List[str], config) -> List[str]:
        raise ValueError('Adapter has to implement a translate method')
