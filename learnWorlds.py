import requests
from bs4 import BeautifulSoup

def scrape_and_save(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    with open(output_file, 'w', encoding='utf-8') as md_file:
        md_file.write(soup.prettify())
        
cookies = {
    '_ga': 'GA1.3.1206642241.1713866375',
    'newui': 'canary',
    '_gid': 'GA1.3.503831708.1729604809',
    '_fbp': 'fb.2.1729604809392.638322744462457033',
    '_ga_G0VV8DRES7': 'GS1.3.1729604809.3.0.1729604809.0.0.0',
    'slim_session': 'xwumqw9R1PJ9n042pt3ezynU5yNy3q1YKpAPdPMO',
    'lw_tokens': '%7B%22access_token%22%3A%22J3lcz66Kn4lS0BEJkV1n34A86qi2f6HSJrAyGXAc%22%2C%22token_type%22%3A%22Bearer%22%2C%22expires_in%22%3A604800%2C%22refresh_token%22%3A%22HvHT1cgNJy7T5RTyX5OJUHKcUIO5RvzXbOMSl2iU%22%7D',
    'school': '{%22ping%22:1}',
    'cf_clearance': 'StWQ3XbvRxxJLMUcHS_k6BlxgtNeubYR284UKq2m8wM-1729675213-1.2.1.1-lBIoeFj3hEK0fPiS8wSrY5dXZ3wHuSDpiQTpancQJV3lKxhUelx.KNdJhaN.T8feRKS59lfcp_inRMZHfPUEZhZZsfFpYzwJIzcCuqBWPatIJYMlYPpqga34.gDldgDsQUU5P7CoobHnB8JJ2zNjXCnPEcZSFi_blFTRzhbSFBmBMmMi5kzsHyQnE1vkdXYp3F2lo8hLjLsXwGcX1zY1phXprDZ2BO3tAsf__O1IyOIXGDmFbWKZZyCa2W5LASx4Qhl3LrhRUVLn3D65FJj8ApyO4No9X.W50NQ9mOuweSwDU4tBpkZ306CbJ3HsH6LDTty9fvDRv.jXrULPtDq3FrlXl6zf4CEb8jlHgrxsIShTzb9TMGOtbmfRlJ2MKeiw2JtK6dpq5lVpzyMwxA3sNw',
    'TawkConnectionTime': '0',
    'twk_uuid_65d4d7e58d261e1b5f62cccf': '%7B%22uuid%22%3A%221.bJsCwEXgRBXDd8B5qfULwsUVRYvNqmvcLP5uVGmysbVMBzbjYRKSzfWauzr2h0Nowldd2mRCyIrZvxNPH5uf6IcFBLxUctD2biJQC2Igy6gNJvOtzEl4Nomf8yUxT%22%2C%22version%22%3A3%2C%22domain%22%3A%22schoolofcode.co.uk%22%2C%22ts%22%3A1729675442866%7D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,en-GB;q=0.8,ru;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_ga=GA1.3.1206642241.1713866375; newui=canary; _gid=GA1.3.503831708.1729604809; _fbp=fb.2.1729604809392.638322744462457033; _ga_G0VV8DRES7=GS1.3.1729604809.3.0.1729604809.0.0.0; slim_session=xwumqw9R1PJ9n042pt3ezynU5yNy3q1YKpAPdPMO; lw_tokens=%7B%22access_token%22%3A%22J3lcz66Kn4lS0BEJkV1n34A86qi2f6HSJrAyGXAc%22%2C%22token_type%22%3A%22Bearer%22%2C%22expires_in%22%3A604800%2C%22refresh_token%22%3A%22HvHT1cgNJy7T5RTyX5OJUHKcUIO5RvzXbOMSl2iU%22%7D; school={%22ping%22:1}; cf_clearance=StWQ3XbvRxxJLMUcHS_k6BlxgtNeubYR284UKq2m8wM-1729675213-1.2.1.1-lBIoeFj3hEK0fPiS8wSrY5dXZ3wHuSDpiQTpancQJV3lKxhUelx.KNdJhaN.T8feRKS59lfcp_inRMZHfPUEZhZZsfFpYzwJIzcCuqBWPatIJYMlYPpqga34.gDldgDsQUU5P7CoobHnB8JJ2zNjXCnPEcZSFi_blFTRzhbSFBmBMmMi5kzsHyQnE1vkdXYp3F2lo8hLjLsXwGcX1zY1phXprDZ2BO3tAsf__O1IyOIXGDmFbWKZZyCa2W5LASx4Qhl3LrhRUVLn3D65FJj8ApyO4No9X.W50NQ9mOuweSwDU4tBpkZ306CbJ3HsH6LDTty9fvDRv.jXrULPtDq3FrlXl6zf4CEb8jlHgrxsIShTzb9TMGOtbmfRlJ2MKeiw2JtK6dpq5lVpzyMwxA3sNw; TawkConnectionTime=0; twk_uuid_65d4d7e58d261e1b5f62cccf=%7B%22uuid%22%3A%221.bJsCwEXgRBXDd8B5qfULwsUVRYvNqmvcLP5uVGmysbVMBzbjYRKSzfWauzr2h0Nowldd2mRCyIrZvxNPH5uf6IcFBLxUctD2biJQC2Igy6gNJvOtzEl4Nomf8yUxT%22%2C%22version%22%3A3%2C%22domain%22%3A%22schoolofcode.co.uk%22%2C%22ts%22%3A1729675442866%7D',
    'priority': 'u=0, i',
    'referer': 'https://learn.schoolofcode.co.uk/course/soc-onboarding',
    'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36 Edg/129.0.0.0',
}

params = {
    'courseid': 'soc-onboarding',
    'unit': '65be2ca7536e31c52c0c3388Unit',
}

response = requests.get('https://learn.schoolofcode.co.uk/path-player', params=params, cookies=cookies, headers=headers)

scrape_and_save(
    "https://learn.schoolofcode.co.uk/path-player?courseid=soc-onboarding&unit=65be2ca7536e31c52c0c3388Unit", 
    'output.md'
)
