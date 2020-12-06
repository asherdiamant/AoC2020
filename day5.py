

class BoardingPass:

    def __init__(self, code):
        self.code = code
        self.row = int(code[:7].replace('F', '0').replace('B', '1'), 2)
        self.column = int(code[7:].replace('L', '0').replace('R', '1'), 2)
        self.id = self.row * 8 + self.column

    def __repr__(self):
        print(f'Row:{self.row}, Column:{self.column}, ID:{self.id}')


boarding_passes = []
with open('data/day5.txt', 'r') as f:
    for row in f.readlines():
        bp = BoardingPass(row)
        boarding_passes.append(bp)
max_id = max(bp.id for bp in boarding_passes)
print('Highest seat ID is:', max_id )


min_id = min(bp.id for bp in boarding_passes)
print('Lowest seat ID is:', min_id)

for i in range(min_id, max_id):
    if i not in (bp.id for bp in boarding_passes):
        print("Empty seat, possibly mine:", i)


