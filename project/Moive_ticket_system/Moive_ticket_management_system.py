class Star_Cinema:

    hall_list = []

    def entry_hall(self,hall):
        self.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, seats, show_list, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        super().__init__()

    def entry_show(self,id, movie_name, time):
        moive_info = (id, movie_name, time)
        self.show_list.append(moive_info)
        self.seats[id] = [[0] * self.cols for _ in range(self.rows)]

    def book_seats(self, show_id, seat_list):
        if show_id in self.seats:
            
            for row,col in seat_list:
                # r = int(input())
                # c = int(input())
                row = int(row)
                col = int(col)

                if row < self.rows and col < self.cols:
                    if self.seats[show_id][row][col] == 0:
                        self.seats[show_id][row][col] = 1
                        print('Booked Successfully')
                    else:
                        print(f'{self.seats[show_id][row][col]} already booked') 
                else:
                    print('Invalid Seats')
        else:
            print('Invalid Show Id')
            
    
    def view_show_list(self):
        for show in self.show_list:
            id, movie_name, time = show
            print(f'Movie Name: {movie_name}({id}) Show Id: {id} Time: {time}')
        print('\n')

    def view_available_seats(self,id):
        if id in self.seats:
            print(f'Avaiable seats for show id({id})')
            for r in range(self.rows):
                for c in range(self.cols):
                    print(f'Seats :({r} {c})')
        else:
            print('Invalid Show Id')


obj_movie = Hall(10,2,10,10,21)
obj_movie.entry_show(111,'Dead Inside','11:00 AM')
obj_movie.entry_show(520,'Spider Man','2:00 PM')
# obj_movie.hall_list('star')
# obj_movie.view_show_list()
# obj_movie.view_available_seats(111)
# obj_movie.entry_hall('Sony')
# obj_movie.book_seats(111,[(4, 4)])
# obj_movie.view_available_seats(111)
print('\n')
while True:

    print('1: VIEW ALL SHOW TODAY')
    print('2: VIEW AVAIABLE SEATS')
    print('3: BOOKED TICKET')
    print('4: EXIT')
   
    ch = int(input('Enter Option: '))
    
    if ch ==1 :
        obj_movie.view_show_list()

    elif ch == 2:
        id = int(input('Enter Movie Id : '))
        obj_movie.view_available_seats(id)

    elif ch == 3:
        id = int(input('Enter Movie id: '))
        row = input('Enter row : ')
        col = input('Enter col: ')
        obj_movie.book_seats(id,[(row, col)])

    elif ch == 4:
        break
        
        



   







        
