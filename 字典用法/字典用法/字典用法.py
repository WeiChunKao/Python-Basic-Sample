name_for_userid={
    382:'Alice',
    950:'Bob',
    590:'Dilbert'
}
#def greeting(userid):
#    if userid in name_for_userid:
#        return 'Hi %s !' % name_for_userid[userid]
#    else:
#        return 'Hi there'
#def greeting(userid):
#    try:
#        return 'Hi %s !' % name_for_userid[userid]
#    except KeyError:
#        return 'Hi there'
def greeting(userid):
    return 'Hi %s !' % name_for_userid.get(userid,'there')
print(greeting(555))