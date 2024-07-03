
from dataclasses import dataclass

from bs4 import BeautifulSoup, Comment


@dataclass
class CVRRegnskab:
    response: bytes
    
    def __post_init__(self):
        self.__parse_response()
        
    def __parse_response(self):
        print(self.response)
        self.__parsed_response = BeautifulSoup(self.response, "lxml")
        relevant_contextids = []
        comments = self.__parsed_response.find_all(string=lambda text: isinstance(text, Comment))
        for c in comments:
            if c == "Aktuelle periode" or c == "Slutdato for aktuelle periode":
                next_tag = c.find_next_sibling()
                relevant_contextids.append(next_tag["id"])
                
        self.__all_tags = []  # Liste med de tags, som potentielt kan være relevante
        
        for tag in self.__parsed_response.find_all(attrs={"contextref": True}):
            if tag["contextref"] in relevant_contextids:
                self.__all_tags.append(tag)
                
        self.__full_results = {}
        
        for tag in self.__all_tags:
            tag_name = tag.name.replace(":", "_")
            try:
                tag_value = int(tag.text)
            except ValueError:
                tag_value = tag.text
            self.__full_results[tag_name] = tag_value
                
    @property    
    def get_all(self) -> dict:
        return {
            "cvr": self.__full_results["c_identificationnumbercvrofreportingentity"],
            "start_date": self.__full_results["c_reportingperiodstartdate"],
            "end_date": self.__full_results["c_reportingperiodenddate"],
            "omsaetning": self.__full_results["g_grossprofitloss"],
            "loen_omk": self.__full_results["g_employeebenefitsexpense"],
            "drifts_resultat": self.__full_results["g_profitlossfromordinaryoperatingactivities"],
            "andre_finasielle_omkostninger": self.__full_results["g_otherfinanceexpenses"],
        }

            
    