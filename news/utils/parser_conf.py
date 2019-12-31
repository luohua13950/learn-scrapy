__author__ = 'luohua139'
import json
import jsonpath


def json2txt():
    conf_dict = {
        "item":{
            "title":{
                "rule1":"//h1[@id='chan_newsTitle']/text()",
                "method":["add_value","add_xpath"]
            },
            "content":{
                "rule1":"//div[@id='chan_newsDetail']//p/text()",
                "rule2":"//div[@id='chan_newsDetail']"
            },
            "source":{
                "rule1":"//div[@id='chan_newsDetail']//p/text()",
            },
            "times":{
                "rule1":"//div[@class='chan_newsInfo_source']/span[@class='time']/text()"
            }
        }
    }
    with open("conf.text","w",encoding="utf-8") as fp:
        conf_json = json.dump(conf_dict,fp,ensure_ascii=False,indent=4)

def read_conf():
    with open("conf.text","r",encoding="utf-8") as fp:
        conf_json = json.load(fp)
    return conf_json


if __name__ == '__main__':
    conf_dict = read_conf()
    for k,v in conf_dict["item"].items():
        #for rule,st in v.items():
            #print(rule,st)
        print(v["rule"])
        print(v["method"])