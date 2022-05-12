class ZjweatherspiderPipeline(object):
    def process_item(self, item, spider):
        with open('weather.txt', 'a', encoding='utf8') as fp:
            fp.write(item['city']+'\n')
            fp.write(item['weather']+'\n\n')
        return item
