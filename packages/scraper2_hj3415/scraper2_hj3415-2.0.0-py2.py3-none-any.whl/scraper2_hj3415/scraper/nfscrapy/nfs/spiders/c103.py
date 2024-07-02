import logging
import time
import scrapy
from utils_hj3415 import utils
from scrapy.selector import Selector
from abc import *

from nfs import items
from nfs.spiders import common


class C103Spider(scrapy.Spider, metaclass=ABCMeta):
    name = 'c103'
    allowed_domains = ['navercomp.wisereport.co.kr']
    WAIT = 1.5

    def __init__(self, code, mongo_client, title, *args, **kwargs):
        """
        C103페이지의 기반 클래스. 세부 페이지에서 상속해서 사용한다.

        :param code:
        :param title: 상속된 C103 클래스에서 입력함
        :param mongo_client:
        :param args:
        :param kwargs:
        """
        super(C103Spider, self).__init__(*args, **kwargs)
        self.codes = common.adjust_arg_type(code)
        self.mongo_client = mongo_client
        self.driver = utils.get_driver()
        self.title = title  # ex- 재무상태표q

    def start_requests(self):
        # reference from https://docs.scrapy.org/en/latest/topics/request-response.html
        total_count = len(self.codes)
        print(f'Start scraping {self.name}, {total_count} codes...')
        self.logger.info(f'entire codes list - {self.codes}')

        # 실제로 페이지를 스크랩하기위해 호출
        for i, one_code in enumerate(self.codes):
            print(f'{i + 1}/{total_count}. Parsing {self.title}...{one_code}')
            yield scrapy.Request(
                url=f'https://navercomp.wisereport.co.kr/v2/company/c1030001.aspx?cmp_cd={one_code}',
                callback=getattr(self, f'parse_c103'),
                cb_kwargs=dict(code=one_code)
            )

    def parse_c103(self, response, code):
        # 페이지를 먼저 한번 호출하여 버튼을 눌러 세팅한다.
        if self.setting_page(response.url):
            # html에서 table을 추출하여 dataframe생성
            self.driver.get(response.url)
            time.sleep(self.WAIT)
            html = Selector(text=self.driver.page_source)
            table_xpath = '//table[2]'
            df = common.get_df_from_html(html, table_xpath, 1)
            self.logger.debug(df)

            # make item to yield
            item = items.C103items()
            item['코드'] = code
            item['title'] = self.title
            item['df'] = df
            yield item
        else:
            self.logger.warning("Parsing error ... maybe 올바른 종목이 아닙니다.")


    @abstractmethod
    def setting_page(self, url: str):
        pass

    def __del__(self):
        if self.driver is not None:
            print(f'Retrieve {self.name} chrome driver...')
            self.driver.quit()


'''
# XPATH 상수
손익계산서 = '//*[@id="rpt_tab1"]'
재무상태표 = '//*[@id="rpt_tab2"]'
현금흐름표 = '//*[@id="rpt_tab3"]'
연간 = '//*[@id="frqTyp0"]'
분기 = '//*[@id="frqTyp1"]'
검색 = '//*[@id="hfinGubun"]'
'''


class C103BQ(C103Spider):
    name = 'c103_bq'

    def __init__(self, code, mongo_client):
        super(C103BQ, self).__init__(code, mongo_client, title='재무상태표q')

    def setting_page(self, url: str) -> bool:
        buttons = [
            ('재무상태표', '//*[@id="rpt_tab2"]'),
            ('분기', '//*[@id="frqTyp1"]'),
            ('검색', '//*[@id="hfinGubun"]'),
        ]
        return common.click_buttons(self.driver, url, buttons, self.WAIT)


class C103CQ(C103Spider):
    name = 'c103_cq'

    def __init__(self, code, mongo_client):
        super().__init__(code, mongo_client, title='현금흐름표q')

    def setting_page(self, url: str) -> bool:
        buttons = [
            ('현금흐름표', '//*[@id="rpt_tab3"]'),
            ('분기', '//*[@id="frqTyp1"]'),
            ('검색', '//*[@id="hfinGubun"]'),
        ]
        return common.click_buttons(self.driver, url, buttons, self.WAIT)


class C103IQ(C103Spider):
    name = 'c103_iq'

    def __init__(self, code, mongo_client):
        super().__init__(code, mongo_client, title='손익계산서q')

    def setting_page(self, url: str) -> bool:
        buttons = [
            ('손익계산서', '//*[@id="rpt_tab1"]'),
            ('분기', '//*[@id="frqTyp1"]'),
            ('검색', '//*[@id="hfinGubun"]'),
        ]
        return common.click_buttons(self.driver, url, buttons, self.WAIT)


class C103BY(C103Spider):
    name = 'c103_by'

    def __init__(self, code, mongo_client):
        super().__init__(code, mongo_client, title='재무상태표y')

    def setting_page(self, url: str) -> bool:
        buttons = [
            ('재무상태표', '//*[@id="rpt_tab2"]'),
            ('연간', '//*[@id="frqTyp0"]'),
            ('검색', '//*[@id="hfinGubun"]'),
        ]
        return common.click_buttons(self.driver, url, buttons, self.WAIT)


class C103CY(C103Spider):
    name = 'c103_cy'

    def __init__(self, code, mongo_client):
        super().__init__(code, mongo_client, title='현금흐름표y')

    def setting_page(self, url: str) -> bool:
        buttons = [
            ('현금흐름표', '//*[@id="rpt_tab3"]'),
            ('연간', '//*[@id="frqTyp0"]'),
            ('검색', '//*[@id="hfinGubun"]'),
        ]
        return common.click_buttons(self.driver, url, buttons, self.WAIT)


class C103IY(C103Spider):
    name = 'c103_iy'

    def __init__(self, code, mongo_client):
        super().__init__(code, mongo_client, title='손익계산서y')

    def setting_page(self, url: str) -> bool:
        buttons = [
            ('손익계산서', '//*[@id="rpt_tab1"]'),
            ('연간', '//*[@id="frqTyp0"]'),
            ('검색', '//*[@id="hfinGubun"]'),
        ]
        return common.click_buttons(self.driver, url, buttons, self.WAIT)
