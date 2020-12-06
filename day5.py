

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
print(max(bp.id for bp in boarding_passes))



