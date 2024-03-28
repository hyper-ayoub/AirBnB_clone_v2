#!/usr/bin/python3
import sys
import requests
from lxml import html
import re

states = [
    ('8b5cb170-faa2-465f-8260-01eafff82666','AbTgYiXzuCytANztHldx'), 
    ('c139ac66-1f97-42b4-88b8-9ad530e11c23','AdQADlZFpiZmYpqfmvkl'), 
    ('c038ccb6-26e9-4690-a1ab-c778679a24dc','AeIXOaMhDANpKORcMegR'), 
    ('26e9475f-59bd-45ee-ad67-c8d843a25fd4','ApGdLZZVNyeLJajXrbzf'), 
    ('c87dc046-b40a-4fc5-8b99-29deb11aa503','BaGTOWpTGMKHJwcJxKzl'), 
    ('dbaeaeaf-14c0-41bb-86a3-ab3da5ba6af9','BcaHPlOptRVGqUEPAqtu'), 
    ('3ddc9a21-5f78-4231-a9f8-1e50f1f385d7','BwSgOREgamofbQBeExyo'), 
    ('103459d9-de48-4cc2-8c20-d03960b8b9ed','CfLrhdByzmzGxQdWYkBT'), 
    ('67ef5d39-9190-4364-bc7b-7b70d7d38a77','CzhicHnoNRxfQOvtYSiq'), 
    ('e138ca8f-9c52-44f5-acce-ef178c3106b9','DaqqQeIunZRrMkJKfGrX'), 
    ('a49d6de7-9828-4a58-a06b-4db6bfe36a8e','DhymLIYEEjsmXEjdZVUu'), 
    ('6a9f984c-3693-4e8c-853c-4537d3a074bd','DkAgpIjzAeYeWJGDyWJB'), 
    ('1aa7506e-3a3a-4649-807c-bb383fee847a','DlVYNgrAwaWlsDBNIsfk'), 
    ('ef0f3e04-9848-43e5-8514-dcc13964c287','DmnIrjlPIljUxErWOYUP'), 
    ('11193dd5-12ad-4fd1-8582-7bf7c1f40cb6','DquEtySWwiVOztMbhjJy'), 
    ('fe76212c-55a5-49ef-84f4-f1b82a709e5b','EaSsmvvzztnSmzDIcRBZ'), 
    ('c3ba8b0b-4261-4b25-8fb1-931f22933fdf','EbtrMvQdSShCQQHUeXIN'), 
    ('c0a22f59-e8d2-4375-b2a0-13e9b2026d0a','EkMKHKlruaeCLvixKwmJ'), 
    ('5e7b75e6-afa4-42e7-9b14-6143c719ba66','ErsQxGUUQpxeOraEOHIH'), 
    ('33632396-41ba-4a88-b0f4-dbd350951f49','ErwbjJJzfyFNDiMYnSAl'), 
    ('e9fc9741-447a-4123-8265-86ae2fa31d9c','EsJWavMpqceyMbcDZyQd'), 
    ('6475cd23-4ae7-42af-8a9b-d9e5c4327d20','EtXnioxqmrqreJfCAwJf'), 
    ('e05646b1-489d-4c5e-9fe6-ebf9676efba7','FbRfgmOBdHpjGZjAeHId'), 
    ('73de5dd8-38cc-4e8a-b247-6cc0b7481f0b','FkeIlfAWgNojeNkAIOQL'), 
    ('604bc4f7-546c-4d40-a712-62ab500009ff','FuAmdeoqnrZSIqcgEqBm'), 
    ('86a776c6-0d37-447d-aabb-98e42d954343','FuwEhNcPyajfjnsjrJJL'), 
    ('0fccdf2c-c5bd-48ec-aa82-874381d13283','GaXdlzZHnoLgJCdMWLij'), 
    ('38184ae4-6202-4398-9558-598e3ae4edad','GbvuYzKPufYtqFbYpups'), 
    ('467495f5-e987-4bad-a8d8-03cc05e3da34','GrfqrdzeTyoFGZNsIDMO'), 
    ('12367838-fddb-4814-a4c0-b5e3c98304ea','GsbHzBSWsDNFAeijAMoT'), 
    ('deb3f633-189b-4138-aa6d-5d39a64f7fc0','GtcSdbyeSZMSuypeGfZY'), 
    ('29f8a6d1-d059-459a-b408-56279def6121','HkHeuWkKvCZEUcDziLWd'), 
    ('84795171-794f-48b7-b50f-ef423ab4136e','HoSzeuMThOxiIVDQnSVZ'), 
    ('8e304ca6-f979-4128-a576-119277344de9','HuozPtKDxYuuypeqxCZU'), 
    ('ae961bda-dfd8-427f-9f7b-668ff961dff8','IdOoCAyVJpJHGfiwjvzL'), 
    ('a0e47ba5-c646-4c86-888a-02f6c7084c18','IkvzKsxMixcioareRcMt'), 
    ('af54cabe-8530-4ef1-aceb-96a3ce5f0e88','IrDWmhlpcytDvlzoqngj'), 
    ('61e5873a-fee1-411f-96c0-270d7a6cd515','JbXNgKmYzhQGKytrCFnQ'), 
    ('d1badf19-433b-45a5-aa00-92ed1cdcd497','JcTTuIHcvuNVQoGhKDro'), 
    ('0e52aeb9-03ff-4b9b-b365-e4d6313471a7','JtdWFYWbyCzRzVjnvQdk'), 
    ('580381ba-ce7b-424c-a697-51769c965d87','KaAAEOkODOlVtHMHwXaB'), 
    ('dbc93795-e59f-4532-a09e-c3f50b8e3770','KblHqFwKYjWyVLPNffIy'), 
    ('56b5aaaa-86dc-4427-b500-90cc3ff7e2aa','KdQtNWbSdSvkimwnMWax'), 
    ('8eebe9d2-4303-41e4-90a7-91a4bc52b450','KrvDSdCjDVAypvJsVvZG'), 
    ('791a7a9a-2842-4343-98a3-663241fd5dd7','KtHtZuITMHRrACWmvCGF'), 
    ('2342dd3e-cb3c-45bc-a841-175fb7a6fffb','LdcmDxCpKqbbEMoxeFJH'), 
    ('fd9da8c2-fd9d-4dbd-a8c5-dca561a75131','LeauBGaGKsfwRIYqLoyk'), 
    ('b9170d3d-2731-4bfd-8045-137ab389fe36','LektKNHhmYVuXhQSMjux'), 
    ('6530930d-8c9c-46bf-8fea-764262d0364d','LuwTjzKGIKuafffhBpDJ'), 
    ('7f44c4dc-4cb3-444f-bc27-71d8d331b72b','MlrewLfDFanbMuSijLLJ'), 
    ('83630e99-a097-4afc-80b4-0b562e359e80','MvhvgRhJhjnqYadQOjah'), 
    ('f9cc9def-4bf2-4f09-9d7d-06b7284047a3','NvLbHqKdxqWWHhLAcPGa'), 
    ('cfa4325a-bd8a-4b03-ad2e-f71598f6c893','NwueTaorIsYOWhKjmSmW'), 
    ('490bc338-2bc9-4831-b6d1-5824cc0a0857','NxCzpgJQnLbUdVLPxWQt'), 
    ('426d30ef-9e8c-40d7-8be6-3e9800a930a6','OmDpKAZSnwrRxVPZNYwm'), 
    ('e6b24870-745e-43ee-9544-b5e50b702c1a','OrhKmyFASaARmYRYEfxi'), 
    ('04921cf3-4d4d-4eb4-854d-68c75c640963','OxYaGUytnDrtpJotVxuQ'), 
    ('dda3e4c9-1c19-4d7a-bcc7-5202a5043b41','PaQwRcHagwNyBqoEwoZO'), 
    ('9bc4640a-ac62-418b-a6bc-20f98568db8a','PdQHxdRRsjfOydsfGTv'), 
    ('91a73216-0568-4448-b224-2dd6ee7d090d','PoAvZAoeMBGtdSyOQRQz'), 
    ('7ca80219-f06c-4663-af12-0538db72ee88','PpzRRIeNiZZaovwyBOeF'), 
    ('069c65b5-a770-49bb-9084-47dff0e76efc','PrzQgwwRvaIzKEEVLTAH'), 
    ('3826a82a-962e-49e4-84df-2362023ceeae','QcTwxjXozujkeXNohOPO'), 
    ('cae4abbd-9f0b-4d37-b36c-9f2384bb7162','QdGMABZBbqFSWWHDAsjm'), 
    ('06ca4de4-8e8e-4bbf-a6dc-d94ed0d59880','QnBjZUxlFQIylJdyIkHS'), 
    ('22005f31-dfaf-4b0f-ae36-4edcd92f3223','QywjWwtjiThdJdNkrQtW'), 
    ('1e13298b-2311-4130-a4ad-f9181fbea28c','QzqOvsCgVGMLbjvlZjJO'), 
    ('028b4563-fb93-4052-89b3-968ab884207e','RazvrlcfpMNvhWheJDXL'), 
    ('89318e6d-e454-4ac0-bb6d-7d0316748d26','RbGumzZaZMvOFssCpMKe'), 
    ('a5a968c5-8bde-4424-bf8a-ce0c28ec45c0','RcGFCoNQiMpDXvJHQFkS'), 
    ('b6a6b90c-8844-4697-b6e5-2068ec7e11e1','RelplmcOuwhruoqhdZSv'), 
    ('2f4b69cd-f1e6-4c4c-94c1-c6872361a139','RfjbODGhCgnSuYxbxGvH'), 
    ('399b4716-dbb3-4c7f-a86a-83bf806a08d4','RgjbyyoVNRSqaKwlQbLH'), 
    ('7c595edb-c69c-4fee-afc1-04cd50b4d49e','RhIJuAFNEPcDwSPmmgOl'), 
    ('1f1a5886-3c28-4631-996d-dd0faf8bd108','RtAenXHfyNwLANnHZAjq'), 
    ('821bb528-ca4c-4855-9c0f-f82d1b624ffe','RzUsRlAgZTbgabHFORtZ'), 
    ('f836250c-68b9-4770-b686-5fe0b43d7a81','SbmHepilkodpWpfgwDdT'), 
    ('dfd26720-d5db-49d6-84f7-150e4f999f30','SdtstpwpGmldwuhoLySb'), 
    ('af01222e-832a-454b-9da3-b00b545f5ac7','SqIosJNcMZRMCQNFkiiF'), 
    ('19b0e4c8-9385-40f1-9073-fe55bb82c1ac','SscNErjzHeQaYIMHhUiF'), 
    ('ec25ffd5-357f-4182-a382-180a25e9719f','SzPLhpUTfdhgVcmzyvwb'), 
    ('9d7eebf5-441e-44ce-91aa-4cce1b7ad840','TkPAbiwUXzVPiTpZRVuE'), 
    ('3806bed8-0244-4a43-8d57-e31ca5098d4d','TtCRhTRcLpjwxNCfSOQq'), 
    ('66754635-c033-45af-adbb-d0862cde5456','UagToFPTYdgxLHinonvE'), 
    ('7e26fdb3-d0f7-4225-9ac3-01f81a79075a','UcpZlAogNhzMdYwiwdeh'), 
    ('7e02a59c-8349-4981-be46-22f23aefdf65','UeGxeJwXOkspgxqQiZPC'), 
    ('8b4c1c92-0daf-46cc-8c25-0fdf8ac28599','UrZMjpVDaLRbegoiwOLk'), 
    ('551ed7b5-25e2-4030-8022-902d4a4bd81b','VasPPAWYvrNYfuUgZZbU'), 
    ('d653d163-ca48-434a-ae0c-321bac8279b3','VfrmIOIEYGXQmGQrBjsv'), 
    ('ad0cb557-8533-4408-83d5-c5aeb9618a2f','VopKqWRTJfFgmLqldITm'), 
    ('31c5fac0-deb3-4c1d-9792-8b53d23bf292','VqUHGjjrcqeEKgddraDD'), 
    ('c53f12c9-8986-451d-a8e6-18365861722e','WMIrmiuIEmINmuOGYEIY'), 
    ('71221ccd-4524-4b1c-81d8-4d38017a506d','XasiTgSUCAgwDtboZtph'), 
    ('5b4415ea-178e-4151-b886-c2ba97e5c780','XflxKWfcoEJDUJYijNRG'), 
    ('898c79df-15d3-4ebd-81d8-c0d24ee66b54','XpCHGjgdZWAGIkMBYpRA'), 
    ('06a0b88d-0d82-4eba-9539-1167f315d218','XqjFFHnHuZGgybArELig'), 
    ('43dea875-d10c-4ba4-a033-469e3dc55f2b','YfewYxJPsejnIbpQlhcm'), 
    ('2070dcf7-f14b-4e5f-8bb3-f3fde2307ba6','YrAoxxsvgJjCCZHNAszq'), 
    ('828a5163-3d59-43ee-9c8d-72ca26d1f3c8','YsXlDVOqQDHYQTzYbwaP'),
    ('2fc51f18-45ab-4dfb-931a-47a0da13ab33','ZjqjfhTaplEnkKAivgor')
]

NO_PROXY = {
    'no': 'pass',
}


## Request
page = requests.get('http://0.0.0.0:5000/states_list', proxies=NO_PROXY)
if int(page.status_code) != 200:
    print("Status fail: {}".format(page.status_code))
    sys.exit(1)

## Parsing
tree = html.fromstring(page.content)
if tree is None:
    print("Can't parse page")
    sys.exit(1)

## H1
h1_tags = tree.xpath('//body/h1/text()')
if h1_tags is None or len(h1_tags) == 0:
    print("H1 tag not found")
    sys.exit(1)

if not re.search(r".*States.*", h1_tags[0]):
    print("Title `States` doesn't found")
    sys.exit(1)

## LI state ID
li_tags = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in tree.xpath('//body/ul/li/text()')]))
if li_tags is None or len(li_tags) != 100:
    print("Doesn't find 100 LI tags (found {})".format(len(li_tags)))
    sys.exit(1)

for li_tag in li_tags:
    is_found = False
    for state_tuple in states:
        is_found = re.search(r".*{}.*".format(state_tuple[0]), li_tag)
        if is_found:
            break
    if not is_found:
        print("{} not found".format(li_tag))
        sys.exit(1)
            
## LI state name sorted
li_tags_b = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in tree.xpath('//body/ul/li/b/text()')]))
if li_tags_b is None or len(li_tags_b) != 100:
    print("Doesn't find 100 LI tags with B tag (found {})".format(len(li_tags_b)))
    sys.exit(1)

idx = 0
for li_tag in li_tags_b:
    if not re.search(r".*{}.*".format(states[idx][1]), li_tag):
        print("{} not found or not sorted".format(li_tag))
        sys.exit(1)
    idx += 1

print("OK", end="")
