from .Common import Common


class GhManager:
    def __init__(self, common: Common):
        self.url = 'https://apply.gh.or.kr/sb/sr/sr7150/selectPbancRentHouseList.do'
        self.common = common

    def get_opening(self):
        self.common.find_element('//*[@id="search_state"]').click()
        self.common.find_element('//*[@id="search_state"]/option[2]').click()
        self.common.find_element('//*[@id="search_btn"]').click()
        result_text = self.common.find_element('//*[@id="sub_content"]/div/div[2]/div[1]/table/tbody').text
        if '자료가 없습니다.' in result_text:
            return None
        return result_text

    def get_receiving(self):
        self.common.find_element('//*[@id="search_state"]').click()
        self.common.find_element('//*[@id="search_state"]/option[3]').click()
        self.common.find_element('//*[@id="search_btn"]').click()
        result_text = self.common.find_element('//*[@id="sub_content"]/div/div[2]/div[1]/table/tbody').text
        if '자료가 없습니다.' in result_text:
            return None
        return result_text

    def get_offer(self) -> str:
        self.common.set_driver(self.url)
        result_data = ''
        opening_data = self.get_opening()
        if opening_data is not None:
            result_data += opening_data
        receiving_data = self.get_receiving()
        if receiving_data is not None:
            result_data += receiving_data
        return result_data
