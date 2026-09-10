def run_on_zooj(f):
    def wraper():
        import datetime
        now = datetime.datetime.now()
        minute = now.minute
        if minute % 2 == 0:
            f()
        else:
            print('Hisss')
    return wraper

@run_on_zooj
def say_hello():
    print('Salam! hihihi')
        
say_hello()