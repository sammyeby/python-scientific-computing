class Rectangle:
    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, wth):
        self.width = wth

    def set_height(self, hgt):
        self.height = hgt
    
    def get_area(self):
        return (self.width * self.height)
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture." 
        with_str = f"{'':*^{self.width}}\n"
        pic_str = ''
        p_lines = 0
        while p_lines < self.height:
            p_lines += 1
            pic_str += with_str

        return pic_str
    
    def get_amount_inside(self, shape):
        return int(self.width / shape.width) * int(self.height / shape.height)



class Square(Rectangle):
    def __init__(self, length=0) -> None:
        super().__init__(length, length)
        self.side = length

    def __repr__(self) -> str:
        return f"Square(side={self.side})"

    def set_side(self, side_len):
        self.side = side_len
        self.width = side_len
        self.height = side_len
    
    def set_width(self, wth):
        super().set_width(wth)
        self.side = wth

    def set_height(self, hght):
        super().set_height(hght)
        self.side = hght


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))