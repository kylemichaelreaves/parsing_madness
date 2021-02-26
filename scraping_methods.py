def get_images():
    
    messages = [soups[i].findAll('div', 'message') for i in range(0, len(soups))]
    captions_list, data_src_list = [], []

    for message in messages:
        for msg in message:
            for images in msg.findAll('div', 'images'):
                for figures in images.findAll('figure'):
                    captions_list.append(figures.figcaption.text)
                    for img in figures.findAll('img'):
                        data_src_list.append(img['data-src'])
    
    img_dict = {k:v for k,v in zip(captions_list, data_src_list)}

    return img_dict

def get_messages():
    
    messages = [soups[i].findAll('div', 'message') for i in range(0, len(soups))]
    all_div_messages = []

    for message in messages:
        for msg in message:
            for fig_caption in msg.findAll('figcaption'):
                fig_caption.extract()
            for figure in msg.findAll('figure'):
                figure.extract()
            for a_ref in msg.findAll('a', 'ref'):
                a_ref.extract()
            for images in msg.findAll('div', 'images'):
                images.extract()
            for div_op in msg.findAll('div', attrs={'class': ['op']}):
                all_div_messages.append(div_op.string)
            for br_tag in msg.find_all('br'):
                br_tag.replace_with(' ')
            for abbr in msg.findAll('abbr'):
                for sp_abrr in abbr.findAll('abbr', attrs={'class': ['sp']}):
                    sp_abrr.extract()

            for div_text in msg.findAll('div', 'text'):
                if div_text.next_element.name == 'p':
                    all_div_messages.append([p.text for p in div_text.contents])    
                elif div_text.next_element.name != 'p':
                    all_div_messages.append([' '.join(div_text.text.split())])

    return all_div_messages

def del_duplicates(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item) 
        if item in unique_list:
            continue
    return unique_list

def get_spans():
    num_span_list = []
    time_span_list = []
    author_span_list = []
    source_span_list = []
    for i in range(0, 104):
        for div_meta in soups[i].findAll('div', 'meta'):
            for num_span in div_meta.findAll('span', 'num'):
                num_span_list.append(num_span.get_text())
            for time_span in div_meta.findAll('span', 'time'):
                time_span_list.append(time_span.get_text())
            for author_span in div_meta.findAll('span', 'author'):
                author_span_list.append(author_span.get_text())
            for source_span in div_meta.findAll('span', 'source'):
                source_span_list.append(source_span.get_text())
    time_span_df = pd.to_datetime(time_span_list, origin='unix', unit='s')
    return time_span_df

# naming a variable object will incur problems 
def rows_messages():

    for div_message in pd.DataFrame(messages_flat_copy)[0]:
        remade_text = []
        #Extracting the tag here doesn't destroy the content
        #around the tag
        for br_tag in div_message.findAll('br'):
            br_tag.extract()
        for text_tag in div_message.findAll('div', 'text'):
            for p_tag in text_tag.findAll('p'):
                print(p_tag.contents)
            for op_tag in text_tag.findAll('div', class_='op'):
                pass
                #print(op_tag.string)
            for a_tag in text_tag.findAll('a'):
                a_tag.extract()
            for abbr_tag in text_tag.findAll('abbr', 'title'):
                print(abbr_tag.string)
            if p_tag.string == None:
                continue
            elif text_tag.string == None:
                continue
            else:
                print(text_tag)    
            #print(text_tag.text)