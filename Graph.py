from queue import Queue

def depth_first_traversal(graph: dict, source: str) -> str:
    """
        Implementation of DFT Graph based on Graph dict
    """
    stack = []
    stack.append(source)
    result = ""
    while len(stack):
        val = stack.pop()
        result += val
        vertex = graph[val]
        if vertex is not None:
            for v in vertex:
                stack.append(v)
    return result

def breadth_first_traversal(graph: dict, source: str) -> str:
    """
        Implementation of BFT Graph based on Graph dict
    """
    queue = Queue()
    queue.put(source)
    result = ""
    while not queue.empty():
        val = queue.get()
        result += val
        vertex = graph[val]
        if vertex is not None:
            for v in vertex:
                queue.put(v)
    return result
