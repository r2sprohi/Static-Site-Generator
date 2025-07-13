from textnode import TextNode, TextType
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_nodes = []
            sections = node.text.split(delimiter)
            if len(sections) %2 == 0:  # means that incorrect split has taken (incorrect markdown syntax)
                raise ValueError("invalid markdown , formatted section was not closed")
            for i in range(len(sections)):
                if sections[i]== '':
                    continue
                if i % 2 == 0:
                    text_node = TextNode(sections[i], TextType.TEXT)
                    split_nodes.append(text_node)
                    continue
                if i %2 ==1:
                    text_node = TextNode(sections[i], text_type)
                    split_nodes.append(text_node)
                    continue
            new_nodes.extend(split_nodes)
    return new_nodes

                    

