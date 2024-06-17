import platform,socket,re,uuid,json,psutil,logging,datetime

timestr = datetime.datetime.now().strftime('%d-%m-%y-%H-%M-%S')
logger = logging.basicConfig(filename=f"{__name__}-{timestr}", encoding='utf-8', level=logging.DEBUG)
logging.info(timestr)

# https://stackoverflow.com/questions/3103178/how-to-get-the-system-info-with-python

def _getSystemInfo():
    info={}
    info['platform']=platform.system()
    info['platform-release']=platform.release()
    info['platform-version']=platform.version()
    info['architecture']=platform.machine()
    info['hostname']=socket.gethostname()
    #info['ip-address']=socket.gethostbyname(socket.gethostname())
    #info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
    info['processor']=platform.processor()
    info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    return json.dumps(info)

def declaration():
    return {
        'name':'System Report',
        'behaviors':{
            'mutating':False,
            'dangerous':False,
            'slow':False
        },
        'parameters':{

        }
    }

# parameters should probably be kwargs.
def entrypoint(parameters: dict = {}) -> dict:
    try:
        return(
            {'status':'ok',
             'data':_getSystemInfo()}
        )
    except Exception as e:
        return(
            {'status':'exception',
             'exception':e}
        )