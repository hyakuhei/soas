def entrypoint(parameters: dict = {}):
    try:
        return(
            {'status':'ok',
             'data':'DUMMY performs no actions'}
        )
    except Exception as e:
        return(
            {'status':'exception',
             'exception':e}
        )

def declaration():
    return {
        'name':'Dummy',
        'behaviors':{
            'mutating':False,
            'dangerous':False,
            'slow':False
        },
        'parameters':{

        }
    }