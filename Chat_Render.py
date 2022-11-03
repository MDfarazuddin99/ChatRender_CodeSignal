test_case = [["1","Hello how r u and what is going on"],['2','good ty it has been really long since I last saw you'],['2','how r u?'],['1','me too bro']]
width = 20
userWidth = 10



def render_chat(test_case,width,userWidth):
    result = list()
    result.append("+{0}+".format("*"*width))

    for mesg in test_case:
        # print(f"Size of mesg: {len(mesg[1])}")
        if mesg[0] == '1':
            if len(mesg[1]) < userWidth:
                result.append("|{0}{1}|".format(mesg[1]," "*(width - len(mesg[1]))))
            else:
                mesg_words = mesg[1].split(' ')
                mesg_segments = list()
                mesg_segment = ""
                idx = 0
                while idx < len(mesg_words):
                    if idx == 0 and len(mesg_words[idx]) <= userWidth:
                        mesg_segment += mesg_words[idx]
                    elif len(mesg_segment + " " +  mesg_words[idx]) <= userWidth:
                        mesg_segment += " " + mesg_words[idx]
                    else:
                        mesg_segments.append(mesg_segment)
                        mesg_segment = mesg_words[idx]
                    idx += 1
                
                mesg_segments.append(mesg_words[idx-1])
                        
                    
                
                # print(f"DEBUGGING: {mesg_segments}")
                for mesg_segment in mesg_segments:
                    result.append("|{0}{1}|".format(mesg_segment," "*(width-len(mesg_segment))))
        else:
            if len(mesg[1]) < userWidth:
                result.append("|{1}{0}|".format(mesg[1]," "*(width - len(mesg[1]))))
            else:
                mesg_words = mesg[1].split(' ')
                mesg_segments = list()
                mesg_segment = ""
                idx = 0
                while idx < len(mesg_words):
                    if idx == 0 and len(mesg_words[idx]) <= userWidth:
                        mesg_segment += mesg_words[idx]
                    elif len(mesg_segment + " " +  mesg_words[idx]) <= userWidth:
                        mesg_segment += " " + mesg_words[idx]
                    else:
                        mesg_segments.append(mesg_segment)
                        mesg_segment = mesg_words[idx]
                    idx += 1
                mesg_segments.append(mesg_words[idx-1])
                for mesg_segment in mesg_segments:
                    result.append("|{1}{0}|".format(mesg_segment," "*(width-len(mesg_segment))))            
    result.append("+{0}+".format("*"*width))
    return result

for i in render_chat(test_case,width,userWidth):
    print(i)
# print()