def main():
    beer_song(3)


def beer_song(count):
    num = 0
    while num < count:
        print(count, 'bottles of beer on the wall,')
        print(count, 'bottles of beer')
        print('Take one down, pass it around')
        count -= 1
        print(count, 'bottles of beer on the wall \n\n')



main()
