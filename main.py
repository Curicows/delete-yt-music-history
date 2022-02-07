import rpa as r


def main():
    r.init()
    r.url("https://music.youtube.com/history")
    # before start, login to your Google account
    print('make sure to login to your google account')
    i_all = int(input('how many music do you wanna remove? '))
    i = 0
    while i < i_all:
        i = i + 1
        r.rclick('//*[@id="contents"]/ytmusic-responsive-list-item-renderer[1]')
        r.wait(1)
        r.click('//*[@id="items"]/ytmusic-menu-service-item-renderer[3]')
        r.wait(0.5)
        print('Removed from history: ' + str(i))

    input('press any button to exit')
    r.close()


if __name__ == '__main__':
    main()

