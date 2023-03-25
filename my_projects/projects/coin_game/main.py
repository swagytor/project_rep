import coin


def main():

    my_coin = coin.Coin()

    print('Эта сторона обращена вверх', my_coin.get_sideup())

    for _ in range(10):
        my_coin.toss()

        print('Подбрасываю монетку...')

        print('Эта сторона обращена вверх', my_coin.get_sideup())


if __name__ == '__main__':
    main()
