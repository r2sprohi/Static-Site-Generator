import re
from enum import Enum,auto
class BlockType(Enum):
    PARAGRAPH = auto()
    HEADING = auto()
    CODE = auto()
    QUOTE =  auto()
    ULIST = auto()
    OLIST = auto()

def block_to_block_type(single_block):
    if not single_block:
        return 
    if single_block.startswith(('# ','## ', '### ', '#### ', '##### ', '###### ')):
        return BlockType.HEADING
    elif single_block.startswith("```") and single_block.endswith('```'):
        return BlockType.CODE
    elif single_block.startswith('>'):
        for line in single_block.split('\n'):
            if not line.startswith('>'):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif single_block.startswith('-'):
        for line in single_block.split('\n'):
            if not line.startswith('- '):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    elif single_block.startswith('1.'):
        i = 1
        for line in single_block.split('\n'):
            if not line.startswith(f'{i}. '):
                return BlockType.PARAGRAPH
            i+=1
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH
            
def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    blocks = [block.strip() for block in blocks if block.strip()]
    return blocks

