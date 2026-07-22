def make_readable(seconds):
    hours=0
    mins=0
    sec=0
    if seconds<0:
        return 'error1'
    else:
        hours=seconds//3600
        mins=(seconds-(hours*3600))//60
        sec=(seconds-((hours*3600)+(mins*60)))
        sec=int(sec)
        x=str(hours)
        y=str(mins)
        z=str(sec)
        if hours<=99 and mins<=59 and sec<=59:
            if hours<=9:
                hours='0'+x
            if mins<=9:
                mins='0'+y
            if sec<=9:
                sec='0'+z
            clock=str(hours)+':'+str(mins)+':'+str(sec)
            return clock
        else:
            return 'error2'