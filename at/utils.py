# - *- coding: utf- 8 - *-
import unicodedata

# Help select Box
def select_box_by_objects(objects=None, field_key="id", field_value="name", selected="",  name="", id="", cls="", style="", first_option_text=""):
    results = '<select name="'+name+'" id="'+id+'" class="'+cls+'" style="'+style+'">'
    if first_option_text:
        results += '<option > -- '+first_option_text+' -- </option>'
    if objects:
        for item in objects:
            key = str(getattr(item, field_key))
            value = str(getattr(item, field_value))
            if key == str(selected):
                results += '<option value="' + key + '" selected="selected">' + value.encode('utf-8') + '</option>'
            else:
                results += '<option value="' + key + '">' + value + '</option>'
    results += '</select>'
    return results


def select_box_by_list_disabled(list=None, selected="", name="", id="", cls="", style="", first_option_text=""):
    results = '<select name="'+name+'" id="'+id+'" class="'+cls+'" style="'+style+'">'
    if first_option_text:
        results += '<option disabled> '+first_option_text+' </option>'
    if list:
        for item in list:
            key, value = item
            if str(key) == str(selected):
                results += '<option value="'+str(key)+'" selected="selected">' + value.encode('utf-8') + '</option>'
            else:
                results += '<option value="' + str(key) + '">' + value.encode('utf-8') + '</option>'
    results += '</select>'
    return results

def select_box_by_list(list=None, selected="", name="", id="", cls="", style="", first_option_text=""):
    results = '<select name="'+name+'" id="'+id+'" class="'+cls+'" style="'+style+'" required oninvalid="setCustomValidity(\'Lựa chọn là bắt buộc\')" oninput="setCustomValidity(\'\')">'
    if first_option_text:
        results += '<option value=''> '+first_option_text+' </option>'
    if list:
        for item in list:
            key, value = item
            if str(key) == str(selected):
                results += '<option value="'+str(key)+'" selected="selected">' + value.encode('utf-8') + '</option>'
            else:
                results += '<option value="' + str(key) + '">' + value.encode('utf-8') + '</option>'
    results += '</select>'
    return results

# Constant
REGION=[
    (1,u"Hà Nội"),
    (2,u"Thành phố Hồ Chí Minh"),
    (3,u"Bình Dương"),
    (4,u"Khác")
]

CAOCH=[
    (1,u'Lương dưới 10 triệu'),
    (2,u'Lương từ 10 triệu - 15 triệu'),
    (3,u'Lương từ 16 triệu - 20 triệu'),
    (4,u'Lương trên 20 triệu')
]

CARDTYPE=[
    (1,u"ANZ Classic Credit Card"),
    (2,u"ANZ Gold Credit Card"),
    (3,u"ANZ Platinum Credit Card"),
    (4,u"ANZ Travel Platinum Credit Card")
]

