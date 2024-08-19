""" def canUnlockAll(boxes):
  box_open = set()
  for i, box in enumerate(boxes):
    if any(i in inner_box for inner_box in boxes[:i] + boxes[i+1:]):
      box_open.add(i)
  return len(box_open) == len(boxes)

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))


def canUnlockAll(boxes):
    index_counter = 0
    box_open = set()
    for lists in boxes:
        for elements in lists:
            index_counter = 0
            for index_counter in range(1, len(boxes)):
                if elements == index_counter:
                    box_open.add(elements)
                    break
    list(box_open)
    if(len(box_open) == len(boxes) - 1):
        return True
    else:
        return False """
        
        
def canUnlockAll(boxes):
    """ Method that determines if all boxes can be opened """

    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False

    return True

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))       