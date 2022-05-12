BOT_NAME = 'zjWeatherSpider'
SPIDER_MODULES = ['zjWeatherSpider.spiders']
NEWSPIDER_MODULE = 'zjWeatherSpider.spiders'

ITEM_PIPELINES = {
    'zjWeatherSpider.pipelines.ZjweatherspiderPipeline':1,
}
