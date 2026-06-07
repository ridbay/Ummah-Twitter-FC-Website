<script setup>
import { ref, reactive } from 'vue'

const imageIds = [
  '1urq3UruzcpQ1wAI2CiPGzLSx0rqi_r4K',
  '1AsQrZXU3cuQdw3Kj9cJrvzE5yc872QyN',
  '1OAe0GgRspsJpEqA07dTRMS7n8ZTSX039',
  '1pTRxt7SM8LI3rVucMH5bHJIwu6hwgyWw',
  '1-Q70kD590ss-wpwLhpcD5oSBE__NvJVE',
  '1mpsvzPMxhT6_hnMYPEnIa0vEjdyG1Raz',
  '1MiV8bnXr75run_SbBpflB2hXVcB_426F',
  '1jbQyr4JdWOAjuf9_LfX2VApdfqIURaRM',
  '16AwKMCE3ZOve7qYBJthuMSv3Q1Tsw-Np',
  '1EAk9wSsrDRECsJ95Pa9lPw82XHaBEPqm',
  '1U9Mpxnd_Hs8QO8NTzzNebl04HN-TlEox',
  '1MMHMnjoP9zUWeSJFdr_0L8dEVmzmRP0h',
  '1wPL77G4hyi4qRtT8JMWHNlAgKk8idpWa',
  '1th_WGFVNAfNaxJeiU5ZbTAIadE8SMXcb',
  '110mR1P5VtuRLM_poiE9-Syioo1jDubZS',
  '1HsqBA2bkLsGyPl9cE9YxzWXHQGf3a-FO',
  '1PZLqGm0O1DbUSyPGZi6UtsK7w1WeA7ic',
  '1ltmKKhuaHLvk-pYwwoH6gkZqiGTXdBMl',
  '13CV1y4kb8CYc3eM3QGNMdph4m1sHHH-q',
  '1utMeVIfIxAgbE2iYRpFi4sjs8q9flSj6',
  '1nNk0XqeswU9ooq_QZ_-sFr-wdaDhEAVs',
  '1f7ZNBHtXE22TE6uWR2NNvJiN3rOqWXpC',
  '1JDTqCtWY5mFqSoJqj9uM88ETWatgWhMN',
  '1sFO3ew-qhPXbLGrYGDdNfNvGKqug5tH2',
  '1BdfXm5atXScO9KHQSDRiZdHiK8Jt_Mr-',
  '1GPj-UOi_Qyyyw65xYlEGslKDg5YcRBTQ',
  '1UomhsvdqGFSnJpYk3AkLiIQsKEfOqjP7',
  '1KzmCO-zB-R3l5bWQ5icxnhlrNqvpPea3',
  '1Pi6Op458sXwO2zx2XbeN7YoOu7aD7g1E',
  '1UNBsdReDzUnLbNLbowzA_Kycj-7yGwV5',
  '1qQ3fbGebEqKGabin71BnZjj8Rh5-yQN4',
  '19fMQ5meYjriCfSnqIdpu3xoSVp-bXBf1',
  '1VmfuHoAb9qM9MPYvkske3mjRhIV0X8Lf',
  '1JvgFGfvyjRVaIrRW7JxmKzpxZp2qWY9e',
  '1PHEqsh-L6kBBw6M8OawIQXy1QPlaowN3',
  '1UHxxozR3Mapszgl25czFUeEunDEQrC9i',
  '1UkJs7LAUbX5gNzKIYImEi4vLAyZjkd7D',
  '1vsu6S14NPiCDUw6IghJDv58sEAneAa2q',
  '1XVw8FXpLesW9rSGKM575nrBVUIcPjty3',
  '12-XGRipgQvF-358mqPl6sRylFpkb8obS',
  '1L4GZUdwNvptSWabP9VVkQEpEnXDFs8ar',
  '1yPvJ5MhSFSoWs8i6LWTkFwf0lDDMn2yO',
  '1O8jiLypAeTbesvRkRS8-txhMrEKJdNgI',
  '1G3LkNtcjY1Sq7OolHaT5nmoWTEZZvdw7',
  '1kVo_UDtCLkK5mPXg2-zFzifi7A7gPXVM',
  '1pmrt2SeRcoi18cZ8wfgf2GiDIWlkHAbA',
  '1N3Y6j1l8JmBQ-aoizrOKmOoXy6z_G85q',
  '1NUyRSH9XYotGJfvkxax_3vU0k-6Vpss5',
  '168bJWc4qvNh2M1ftf3BHMjz7tOtnHfDv',
  '1GBbBIgSV4A_SAC4oRWcO6mbJRkhEXtKy',
  '1lEj-MLuv2Ic4-7vTBZzBNNkfBD60OlsF',
  '1qInMmErWV7UsWGCwk_3qg12gx2eKn1Ad',
  '1foxSqO3FgmWw-ysHeGNdzuCtib5cnzVn',
  '1gnHT9Zh1o99wJ3asPqyUYHk9Wdlrub76',
  '1V2Y6O4zjsaWvGGBvQzj1K4QivaxtaAfu',
  '1dvEYcCwK25k9Fjy_YWaYbYIPx2SiBOdu',
  '1Ao04Ns9-WqvtCrVQKR_qgAgJnjcWqfUu',
  '1mgyRtvocDJIbTywLkziPBCSV7NlBk3CV',
  '1BW_HxLbARIwvfN0HwjZCl7iiRtHBmN2_',
  '1SfHe-9bKWDzAgsSl--UKbsWMLRqsT3v9',
  '1ubWI390ZYqxpMCjUuFrIpFhAzMKH6OOc',
  '1WxcsX6ss5m1Eg3zRlvxBzibU4fjtONaM',
  '1Vh_1TLUQuOgrx9eZc_6gywd8sxHqWaQH',
  '1IdbrpIcUvU9wBNRHJPYVznS47SUKqtRB',
  '1Kn1ALV_eexdt6UdSO7ry2tsYNbQgyQpb',
  '1z3UTXdnp-IyE9pbN6OcebQrF0Zbdbepz',
  '1vn_52wKOQOLj1Zsg8LLMRkFm1I2RH4d8',
  '1UcEnNoWTnteVSUQbTKnFdApo28K80YWz',
  '1zRSDA-gu4mSEdyDcts51QMAmDtUVyH1b',
  '1t6ZMC9xWCJV-LuUZxKJLXPdldlkal502',
  '1VSoH5tU8N6xMpbos5_mD3bj-V-cBq58S',
  '16nD_sNkBHTre3OiXAsPb6RXm_WHR23Zr',
  '18aXIe5kAtHZLs-RdN0VYOiT5SMFZJk-S',
  '1mf7e3fvPdOkPIxlmGKdQuCf90JjbJCNR',
  '1na5ZDbVX0X7A8QHWymlubcTZ9uhij-Uj',
  '16UahDy4yCh9_nBkvpL7sO2rFnbBzzJC4',
  '1r5Xlk-6MkKDx-9ekMi0U6qznG3hjxpN9',
  '1IUFB6wetdefwriYNFA7atZ7a_o9zDPI6',
  '1jOZsyiJKY0Q6Psx6PC9zIkAC-KItfEsh',
  '1wUGc1ByMw9dR2Ssq4wPl5voP9C3DM3OK',
  '1pYqh0BVim-pxptitVqs7LzAHxXTzNBH2',
  '1QjAZwNQlZCuDYvz_ly_sDN_IEbUF7eby',
  '19rTXHQr50GeHfk_-vv4RKH36RjlxXJcY',
  '10romZAFSUPA3PHT2OAd2LQ5kZQ4LSAw0',
  '1eGqiWLHEoisXVJnSBT4ohMXf8owHNIYA',
  '1seGeuAVfySWxSEIXzNRN_Z6UjtTxjAV-',
  '1R6PomIN2oY_8V76nICa-IIamBjHXkpm0',
  '1f4H_6MEaMRUAb7iC_dh1ad2ni_rn0Di_',
  '1oGz2KuXhlK42V0J8pO4tBI8PllXTxXuO',
  '1-X2rYS9v84YpFqrWeCaYy8X4te1p-7Ni',
  '1X01mlrHtel8W4kkZ1oC3GYjd_MCc4aey',
  '1G-4qg72c1SIsLc7T9yM6mnkEJVKyEpSR',
  '1b50uwUKigQGcLcO-eD0KCjc0j7jzCuOT',
  '1LXmwfxPja2RJivdOS1_S1NmBKOUncHyP',
  '1SDQw1QSyyrLKZ7XNQ8GzgiMjtbuGIAXQ',
  '1od7nOectC0QM03mYdzsil32ZmEyQdFbC',
  '1OUiBESMt3xuDRl1olQZcCeexGCqDMHcF',
  '1FHT4Ne0Oea0zQFSQnfE-fyR963sw7_7d',
  '1lwZfVxiPtzluzQtLwU6qnHBJGnuEdCzH',
  '1pZQ8i32ONVue-bE5I5CF4x0IEJUpvtKO',
  '1eDWVbiPs_q8Ntj-LT2EyJHZVl587ekQN',
  '1TfIKlK8No1CItuQwltPe413vtJwtgcy3',
  '1OUMUY4G-Pmu33e34kds7A_MrMMP9P9p4',
  '1mvqcSyv1lgN3AcuLslvr2sVZPHdUtqM8',
  '1KzQqZL271Tc9MklRTYDts43b9LX9AtNc',
  '1Lh8iSu-c9UzzynZYjOr8vNoOzzrZiqJg',
  '1gsgOxn7cWhhXH3goIqXtleB6H7zMhJ7z',
  '13VmYzasM76BYJvXGR2deT5Dy1h60oOhS',
  '1mwZecIYo6wE_xPK1k3W3I4j2iP_ZgF89',
  '1YuT9TVC51-dsZG2EGOx_rQiNwjIdEguW',
  '13orbjLpojSCoBej-pv1V-fnGUk9xTuUQ',
  '1f6vMYMT-blc1-HD3gIh9SVr4CyXnb3e_',
  '1bK-6vGXKTDI-fewGa9FYMAyjKCI86-p9',
  '1mhZZpdcSzBHNGrTEwe5h4hXxFy7HpCBB',
  '14LDO5hDrUP0Bc21Lj6Kfmg_OPlvPyaqz',
  '1msXh0WMNIKTqKtFstItDgJ96dC89qEVf',
  '1jpWao1uYViYybQlj3dKTkuaP3rM3cjGU',
  '10CYd_kynpgA_cfyMrfLTTHVxLD73dwBH',
  '17FrN6xR9LGAEPytqA_-L0s_aBVJyQUHC',
  '1mXYDSXWLEHTxFpNs3-H6Y_99Y3YFezqg',
  '1xLiXoE6JYgvfi7e49dx5mP6sIj1dW5aC',
  '15aCum5e2ISh55saFPLEhd5gS3UsmKnad',
  '1YN330q5GlOHcz4COgwvVSBnidKEsmWfd',
  '1mnfFxsC5Y7ZvHxLe84XHjZyFuChQ3vNe',
  '1-ODx7jbG3yUn4JqPKYIEf1JGeUSPJGaN',
  '1vxsSwv1OELvgfASg0kJeOzMUT76wmZ0G',
  '1ZEeFAVb8Ac-z2qnNE_p8L4DERYQGZSB0',
  '1RCpp9qjAjgyizwIb44FOHDzbmD1ou_U2',
  '1CfAc7DhVj2MJc6ITYV96jn6pesOTBHcg',
  '1EVkC_kGxfssUvdkgYyKQmudXowsCwbnY',
  '1GTkNQuCY60GFfPFuxnEA14llbIQa5I7k',
  '19dvQr2gsmoDW4L6L2OPaIU_0QfXfrvLR',
  '1kyN5hYdGHBxvoLIOdW7vx3uSS065XEbW',
  '1PoPnCdYhYYAYuc2QifiesgOiPTTsNJct',
  '1Ns-88PSYbby0N2dXQ-JvjRjPssxMexRD',
  '1657Qjtr4vUN5j_yRc1in8ZnHmlIfDFr7',
  '1Hfv-Dwf-XqVKixp-ZpdRezsu2pyxFrH0',
  '1uMorkwxTIOKf7h__QDNpRp1dT18eqOlH',
  '1QGkuR2NNowxIRqOZ87L50K88TWldclDd',
  '1LD5ooXKaSdAMUjU9RIIM7lrgtUr6d1m6',
  '1joaT2dcelW9cZCBsvBvlk5JCwgcJX8Fv',
  '1PG39zJndT_6GAwDLsUXbvmoIA5eMSiHm',
  '1LYDKEEIhIy1ajZLviQCsNeooOYR0G8UJ',
  '1ks6uxgWvBIr7gZ8G8xj-0EL_dbPTWfiU',
  '1i2S51EU7A_HVH6PD_I00TcyYZKOoIKBf',
  '1chm1ocpD8fOkr3MRr5q9ranSUxcZQZJg',
  '1Q1gq6bgNXmTfh749Uw2JV9UsLt-3I-bQ',
  '1kZdDQekUu4X1qY10aE1X9hB4FKxaywND',
  '1C4zMq0Y9lW_gFT1hulSBQ4TsaUBZ7v7p',
  '1fxKmXdSBE6ZpteJwEx-V6LCwMRBDxtLF',
  '1y3vH3ESa0bcsFGiiM_7kuX69vu9ZDmv2',
  '1U_UWxAr4r9lwKLixd8Ui3lhfyT8JMGgC',
  '17ogy2reYbtt5AM7a4sBdE86T8TX5Y_-w',
  '12FHLf5FExtuJFAWiWQDBD02k3cxZYFP3',
  '1XfehlWt-6NKwLGwobyLy11ckiwIt6M2s',
  '173i_X4JXQ1hgvZnL03kR75fFhhTeg8C3',
  '1hCaZNATBp4rVUQNd48c4stO4eeIrdUUK',
  '12fJTUoY6M0w8wqg0jJhYa5PEi4_e-1MD',
  '1wm5mxo9SEzaHM-3JMj85xAz0BHiqpjPp',
  '183OZ6iSWEIp2LKG0IV6mejvEo7xYp1eU',
  '1yrAyQmHFdqcIv0uQi4loqekNbWpbjeGP',
  '1GVyM6JP3PoIhRo-Ab-o1xCoxlbxiXNfd',
  '1WcO0oNxU7xE8ePrcmLeEI-EO1AIHAE6v',
  '15gMcYNL9LDedAqjB6d7a9Z6Uz67BCc50',
  '1sUoLsCjC16quPhQDdhVZjJ0csWzAtwLo',
  '1ZLHzip-TQhX6gn_z2jbi8vnUQORPN0Sz',
  '1TezZ24NJLRI1UURQTlRBKvR4np_4RAM5',
  '1q2SqhhZFvL1dnRvq_7flfYZN4nNFJShu',
  '1Fnd_37ldd18SAlUudLKDo_sWPedwmG7P',
  '1knb3o0g3Kp-pErhBcPxGWvGSKk3hS2s4',
  '1_cHGRBgDWUUrct_ngxhv722ZVPTUCjsD',
  '1ly2irqOPIU7PmzVXTFA-OcWd3eIvImhW',
  '1wGzgCOFN8cdbKgq62LnCU3ferl9UUrUx',
  '1TeUeJoRruYuO7PZta8LTHAwqDX6PFCTP',
  '11PuPiAmqicR0V-f2BWu0QHmH-9YN_k2_',
  '1IMQ0so8wUYDcegdEwcfWvWm8gHBpizuo',
  '1Ql4iC-LDvcQTPGfma9vFYrfKL1vuibjT',
  '1_7yLgourFkahK6-wWACqehgc856uVIGg',
  '1ARp675fvrjHt5q0UmF-mWUMN1yT4I4wW',
  '1A2ZQveLdj98q6G3r7cAYm53kYKhK-Bgi',
  '14PSk5Q0mI1RUli2e14KmzEDToq1XpXOC',
  '1pQ9wyHgqmAKhrtSDrW28ifAQEwfNScAI',
  '1p7gezXs_2DRoihgAzCINy-ar1fqauQUH',
  '1kb81nv6zTKRaOCRFEqr6aJnIxRedp400',
  '1VD_oDU3P-su4mUp89Y4F_I5SNzFTuvDf',
  '1SYy1SAwdoK21MIpTNGNtjEANECgxTZ3B',
  '1pW_qQLWbOs9ZUiquwAmJvHw_t0-YvM3X',
  '146HixGSSMY3vEbdAYq33Kmy3xk8JDSX1',
  '1A7KQ4y-hNKnsY78SnbjytcC1L7sj_J61',
  '1ZTsXPGz4CSpYrvWwBBjjDRgsManSpgTt',
  '1oBmfvcJoa3iSzFhMrCUu-JAly3nhIEFG',
  '1TAI56esiWto17OdXcWL-dmhCImQX7w0-',
  '1y5UbhWVauAiWkWfaBWdr2wBe5iqm99Xk',
  '1rgfjv2ncbCVdKDqWkETojx64adpHSs0n',
  '1P3VIwi3ZBVHVTse3_SPjknqRKe6aJmBS',
  '1cqh8Xw-A-Kk9AISGIHQtz0oBNZxkvRFr',
  '1--wJEidIbiPFvp_LIHjBvZzqzyvhZEe-',
  '1TBl6P0h9XF7vA5G49WfGDLF-6wFHDOD-',
  '1-75-hOtjn1ZYpPU3fK4aWLXDihMES_4S',
  '1hAN1zHvpsXAdXd-2Z-OcyT257B60v0U0',
  '1tiK5PNm-45lL09188hntDO-jF7faQbpa',
  '1Y7_c9M3BxQ5kLIvhjboljnFj5_iZb0BP',
  '1pOfH3kAvgZCUxCmL16zpNTH8ZZwReShC',
  '1VYqsdPEinKk3E0U3tXVdTc2ZtXSnaflh',
  '1HRBh7luZg2KDGByRLpj019jWMdmSrDM_',
  '1lyXWmEiOLTvm5NnNEe6rVx7vZAaD86Dn',
  '19pEIsAl9vsevzBLQzn-cy2pEA_a7xner',
  '1TLm5ljrOCNmYKOVQGu6KhhXYaB_4rhiz',
  '15SPzdN8eFvSMBNXPxHsiyRVAopEOGv4J',
  '1l5V6mWyt7X_rsYNGeMsysl6FItPIbc6X',
  '1BCuOhwHskgXojRqoYSZJA6GYe72BL5te',
  '1zSTOURiIT9BLC2k6xB_yQ8jq3Wt_JG48',
  '1TGPjAcol4zgZoSQZllvtttG5fbUcqSPi',
  '189gGVjuOd6mABWLelVRksfaqcyW-6oPE',
  '1IgAmdW96nC-nxfJUhSxeMhdTtb4cSWni',
  '1Bn5vQwhkUVpZenYGfdtrgY-g8MLTMw8L',
  '1xCLAN_rT-pdvMa10KDOtFQywVO7JdcwY',
  '1awI_ft61yOgHkqsiNlEMky768yFD_Sgm',
  '1wYxaimdQdQSIF_Qy2Ntj18S_UCpSLtRb',
  '1LXn7W17ZoTBtcprY0pMFpotgF8-mQN_4',
  '1L_v1W2F8mjrMC6lVakaihHbcWDq_wHw1',
  '1CkcwlDoHXZ66u5skbjSuL0D1ZzxRUSTT',
  '1Z1JHofm7D0tRhIWljXkqsb_culB6Fr67',
  '1lhk7tlySmEc6r3XhGPAKSjhH_o0XAe2b',
  '1AKrpsUQQ1oPPDm0LUvNTCoXYFr6Ugm20',
  '1wuAR_q7JRXfvroD_XPW2tKILMHVIFaCp',
  '1Xiq1MxVX9J6yGuiOkcJ7zTmVxT2dso_1',
  '1DvbGUQlC4ChlyyLNyOnn1N8WcbAbqvR1',
  '1CaDbVh_DLXcJ06WhAnoSxo8eN0C_aTI7',
  '1leYDqNWEdjud2wxLPCOI7UxGH4fFtkv9',
  '1h9-XBxVjMdk3AOzdsh1fmy8FzziaVtiR',
  '1M9Vish6y-jy6Zg2KwX3RHMK5CpsNs3xg',
  '1uzBFSkg9mw6g-9cb8itHe8DrNnthmk7W',
  '19i74IDv-HqGw_Zn_Y2P4SpRWuUeLjrBH',
  '1EADRlRwhUr5MJaQAIcjTY_5SGItOdq5h',
  '1L8Ibd9v2CnWIREoXRx85cdQZUUZGNHp_',
  '1STb1ABJZUZatyMP0Bv3e5r6jb0eDJSpy',
  '1-3FxlEGYBg1uDqNz76qENRWDa85Q5v_d',
  '1pvPEYOCtsrpdSGnYP004Tu1MNOwkkHRx',
  '1UL7aXvIjQLYJLpJ_1rS4Pyc9ylXd9fYA',
  '1C1BqraT2VQYiFdg7z3AGGVCnnIDvhhpc',
  '1PdJ3o0BLfdKnpf_2UW_Ff3tvkMiQiRSS',
  '1mnaP6vs8InUlmfHt9yO70iM9BWgxV3aE',
  '1tsw4ZONX_OjC8vmn5QuRZowA33Lwxah0',
  '1Bp_nM8TTyd7srXpkXPDHWG8UQyWEJoqM',
  '1Toz_2s3fxrTILsS7dgIy9VxVyH7NtqIJ',
  '1FtOdSME2MMq0oPKAlCGi0Pkc9OWE6YuT',
  '1XQbZth_viGNnV1m1-ptTdHMTWSkbtW5N',
  '1sIveYghaRYHQn_pvCXIlD6CUzJTp-C2g',
  '1wHyAoc1ktIdO791K1h56eBAABVrGhyD9',
  '1dlredKIEOlfKHCGdRgZLF-yq8qHwlXDM',
  '1bIgBfR3qgS1pI0ZwadJoivdmSNVFl35w',
  '1qhYtbN19Jhu9_iExmoyrKjkfRbb8-Ykm',
  '1_Dedh6eA16rRIhiewj_4GhRZEk6snUzh',
  '1FmoyWgsCPdsMyY3AdKk40ax45ttT_c-Q',
  '1YWiS5N8p2XPfiWIVx9kljfvigDJoRDSD',
  '1OYulbzT2DZJIyEQX17Q6sXxQhZ3n1Pgf',
  '1DpsnBJwyUVo_LgRFUB5l9HzedUuhXKf0',
  '1H7a9-pyjMaoBy-M6TdrU_1GB6kwQaG4_',
  '10Ur71OUsK2it258OOnAsW0-86mYJA7ws',
  '1d2dt0knyXCq6_CmDCTlXSzQfZPGz0ZzL',
  '1d10VtTztiMpxjTkYwbLZSI10V16lTwib',
  '1yBeTW3U1U5pL_tj9lU3b-6mX7aGcOGJ0',
  '1pa518sHxisb2wD--tBqvII3ma-urQHYN',
  '18j_gejVOeaXoRzm5JxvGSHthwpieNK5f',
  '1Rc6QXk28_uIdi-B3Hoqd2pcPn9D8aDr6',
  '1gR2urUv4pYCWJ_hbT6H3Vn_j0gg-M8iD',
  '10VHZpw5eNAylmNG_6Q5GRloqL42FPoAT',
  '1gUk_bOUqNXESNLxCwlRcLa3hkudQr0-V',
  '1e_gkoJIxWJe5ggkan4gsxOIBTqlH3t7g',
  '1bsQsF6pLVo6xubbY2H7ePrPR0Kt52a9x',
  '1ZZxMg1mleLgzlAy_excKZ0oJ4axrF14U',
  '1FgP2hoGkt4jrZQG2TQZJbj8QRzYdUCcg',
  '11SxBFGKXje3lfCSbtcFjwmjg0GYH4F62',
  '1n94GvDuGWu9SSR5N_XrEo3Fte0EAkFTh',
  '1Ycw44i0wjsL_QkbNfClnQt0aku6WjyY9',
  '1cmsGmsbYx2DtXlWs-IlYoulAaqYrbkGj',
  '1o2R3Sz-Uc8VxFthwHV9RE8tCdFhTACnp',
  '11k0xkKop0mecws9dfGxLRQ_ldndvsobd',
  '1WYnB9cLMWNL2UxirGINjnhlRGNUFwIH6',
  '1CoYTx4ga1ZsLRilU2KgtFLNjuzWaJ9Dt',
  '1H_BTFPVJuq2emGSc2Xt_Sdz2IEqCF8WB',
  '1m33RohBCifd1gbEVN35V4GtlZd-mGLn-',
  '1XGOChySSlhtHbHp3EAWhU33iZFPdO38L',
  '13QzDYkaimoSzEE7RhI9o38k9D9aeyaDZ',
  '1pd33eTc0_w4LG4NJQHHeC9wEypVHIdsL',
  '1G4ptS9qenHAz9f2TUaERcqOBZmu5UQHt',
  '1CB3DAaqymKIaMxtQKNUPjx5ErlzeY3ba',
  '1tk7F1qmDN948mzAGyxZi-5NCCxZ76GrP',
  '1Yq9PNDKWYJSsOr48ExrQraOsjZa4M-nQ',
  '1QdDFgEnvIcQwpEiXXQB5eRShP8v9j3Ld',
  '1x_lDDWIe00n6EZ8tvokDV5wnbspf03E9',
  '1jhvrpFxX7FztXd1H7KOEnSoQHLi1O-rz',
  '1H8EDR6j9_V68So5F1eH03o2oFYotEGN4',
  '1R_TlBSfCnYXR_CrUKxV5XGSav4OQxOmj',
  '1dLPAYiEND6UOT5vIt8cDjFb-qcGw2iK7',
  '1XQ8ieZARWOH9dpzhqb2PD4prdXcvuqyX',
  '16hINmYHYhP4xpE_gDyqgtDi0xFuX4Yqs',
  '1AKQ5emMiS9mXL493NcaTEP31PvzoN247',
  '1wpkdO0i72hhoH9crdrhGjEsWQK3UfdNb',
  '1zvf3owLp6i8lqiIwVGoN9ekGDUEmYOjE',
  '1SyvOA0--JlZqCUhITT5sYVRedAvNvhAK',
  '1V-jZhaicGbrUDL6MNOwiu5pyIti3EcnI',
  '1RXTkdATROL5y66_TKF0dAehlL1bO5itp',
  '12sBsGWV0UdeFS7q8v-IC0Lpvxy8HyrMk',
  '19SFMZaNlIxAP3_8wDpHyJdW6ecBiVr_K',
  '14Xd1Zsiu_DeHDfhAxAwJGzWi6gHTPz7P',
  '1kBuDvJL8gwbNRLFCnAczeVrUuVj-iYK1',
  '1jmZpaZRJ38VgOxXaw_-3dX4Du9Kh7uIr',
  '1__BOKAfJzV572d8fZBEm-65BYd3FxRSM',
  '1S1kvyg8idj4iTHO1ZurmpwuupEa2NnnX',
  '1qYql6qgEOm37xr66Org1qncC6ow-4sW6',
  '1x9vbONlj7aWarn4dMbfobHRUh_3TM1qA',
  '18kbrUjsUov1sg3Vj0c4slYOAIIYGlMU3',
  '1ICzs92cxwhTDQnzz1Da4P7dNW_JA7OOo',
  '1Jl4XaDyDdTT9IaJZ6dk3BbIwndFQ-v3C',
  '1pdAx-TFBqr7tOSEFGzML6EqdAU9kCN6F',
  '1blR3Rae19Ewci7u3yHDBlXUG15kee4lR',
  '1zOWwq44Y8aBO-LimNxlamUZUDFMhY1Qr',
  '1Z_QX7DvSZU8YGxV2hJITHmkMnNVj_Qtn',
  '1Atvb3jNWAcNNQOGRJ2lX4sXJkkrc5Pob',
  '1YknsgObH5rlIYf8I8M7LHw3PHC7qJBrb',
  '1395CrkzUZA4PeI0dB6kdtEQsF8NrMTFn',
  '1N3TXtl5wTInge6XLVQaycuUvS1LqStK0',
  '1dkvnTRS2ROgyJIoPIngq_ziqby2RpVBn',
  '1_rcbME8Nbho7FBCciNoREBMqibz02pzB',
  '1uGJIs5gdvNa3kBFi_-AHnNhqdtkQ13Py',
  '1ZMpfV-PdFNf1-CKyVUomvMtfVof50Z5P',
  '1YXiS_ydp_ToU4mD6kiazjEzq2k7qC26S',
  '1O9-Bns6LAISUkspB0n8rXxTlwkp7JPxO',
  '1_Km-MpbSBrGO-pWtByq79WNFg0GQMEiF',
  '1UbUKf8RvqP_en0PbR3uv8v02w9jdSB5K',
  '1F1UikzcIjLQWGoNo3LpMEp_lEmVUpy4i',
  '12VlEOkGPiiJ4hwc9pdhq1qrKYZJsZ435',
  '1tDrPK_xv0GGDl2SLQwBYoLatql5vRgh4',
  '1QlUa8BmyFgTXDaNOVNnYHCnLKKZPZRPk',
  '1cxlrJ8vAL4ewT4G2PQBrEjsJpZ5t0q0R',
  '1h1jwwDgc_yeK3JQaXp6rjuJV1HRDW3xg',
  '1jVVEvoHBDav7mVFXNTYa-fOnuViG15pt',
  '1lBCll6himAI7cYzIUQEPgx6IuTKAr_aC',
  '1XA2SDfb9xVNWG5C-jG99o9ELB8pbX9cC',
  '15JGEn8OLbe0kf_HgM_8XpFUccGp-8Yqe',
  '1FxPkdb9Ny9ImhmRcpgVyVGQnfrIFS2j6',
  '1NqToUzJlwiOaZuLAVeLBbJPvxzVDorI0',
  '14LZEinmtbwOzSTwstjDTVtmJQho8K0KB',
  '1XYovlfMR0yaFggP0cl8XLo-591LJ2pNu',
  '1geCsdNiPIEHF-_pOPEnkLzkQs8c-ZOnR',
  '1Wnw-_W6IrBYKz4g0xxXfr9b0rBrnxUaT',
  '18cyCcBOcJ9wBSKg79p4ytJgwaEo2fMbn',
  '1axmdidx519wXEx7PRmt2tDo7_JCxqQ4w',
  '1PHq2dvxww-HO0XAzvnhiOAb0RHjAZm1N',
  '1uaQqbR5qGSwxVwYeTh-DtS7xocgBSHcy',
  '1z9FkJ2HaeKavGN6zmdAqHD8EegPVNjl6',
  '1YA1Npnu9U_5gXGgeJSh8DXSLXzjPQjP9',
  '1Ut2yot4AsCceX4Jmk5dtwThItzdz_lhK',
  '1Wp8oGG832D6sRMHHFZ4D4WzAHmNmM5NP',
  '1Mly3Syug6nljsNCKQrLu9Kp4G9q8MKx5',
  '1VyKt4V1zGUNcIYTscSra9dJOsj4oymbU',
  '1_KC4-aCWvSvunG1YHYy0l1_FqXSZkphs',
  '1Dgqd6IsMZVpqMgF1yvExeyLgakDHYLM1',
  '1AUKumL58xQvVTW63xoUEtdogpYruqIuE',
  '1JqEeL1G8YRLuonT5U99OdhU4qnlswYsX',
  '1hl-nbmzvHVEZR2Rklzue8m4vrgRHtpaA',
  '1ZJdEL4IDYkZFTsmAAAeuEGayAewE0IaF',
  '1YS83RU7qO3wl1aacQMXgw03jYSdbKZgg',
  '1kijSoABGEmirR0oqj6NCE9CPokKiiZgd',
  '1oTTa3UUVYn5Ar3efQRWPlzlN0RdaMOnA',
  '1fzOKK7qX6b-JVhXRVW2226I7vWZguvK-',
  '1q--JU1LqEeovyTazjFcwsmML7xqGzJqi',
  '1JEm6A3RsZlyxyT8Z4rPY1InMNNvoJtxu',
  '1vl2ydd0STUM_0OQvWQRyT8IFhcPnIAid',
  '1kkCF4POv3_2GNmn-qTiK04_IbopACery',
  '1HKtRexGFvrtStOoDbh4nhpSmqEO33vsF',
  '1_L8BLqGySTEMbloWawWA1sCdeFkk8P8Q',
  '1sQwTYrjaZg5jdZE2mPNQxnN90LPdYITH',
  '1uh5CHFJ9Xy1FTWQM4n_DfDO8twQEkPms',
  '1iTi0r-7-LxzO7Cn5QOYnvNW4lSMbux-Z',
  '1aFp4jDz_dYWPD0-YM5CUzlbhwu7C21ow',
  '1hDqOjtqJzCEhBD9KCw5N8YrOCKmHZMCn',
  '1EgcFwJLlddLywl6o-41X5x-wQHGNFD02',
  '1iGlpt8lHpxAp_oicY_3JXG5km7pLs74c',
  '1-LCG3kvPXj26Y17PC_m3wvquh1kUFl9L',
  '1204DjHPfoz5v3C_5gAHWIMSmo1eGQs-K',
  '1GFmKbse_MrIrJ7PU6pic-7KSkpvlS-KM',
  '1R8qA_MTBvMr6KsC2XwTxI8nprEXt-mvP',
  '1UNlVAd2UxD1w15a8LLxEsavwF0RNVwBu',
  '12h7EuXXnzGx2QSJ4C-ClhkV1z50-QYKs',
  '1EEBz4BL6dDAjZ11G9I3r8BXDUwahsChI',
  '16ZSmZu9_sS_nW8imEkBtF8LFO8MdprbG',
  '1Z4V7-eCCruIG6iftk_yHYZe6B58cp55U',
  '1TM5W78TTeyjLBJHY9qwz1rOA1Eidu5UC',
  '1tzEv1PNMJSi86C2OZaUcoNZtkpb-XZBr',
  '1txvGLqqk6vsHOIyjKNIzuvZV-6QrVhcy',
  '1tkT0tFQQVC349bLWk0SGmljgdXdBykdf',
  '1YydNzRWD43fDTmQhJ5gh6PjoD07FcTAT',
  '1Bk6Mzhk1m0cCZa3dbNOy3WSApL0_0pkF',
  '19wDnzbt51QQrjmkrKuirts3Gqgpb3Hag',
  '1EUfbxblpW0CD3usHt6ep19nPImrivY5R',
  '1p0J14ETmvbRITDnqJJyXLFS2882QSq3X',
  '1m3xcH3OVLMFbZNx8HQgOnOH8LR_vGZ9s',
  '1ng0o9NsV2s59N-JFBYP-GyieVjXdEec_',
  '1YEAMc1qOrXciBcRkRHHsx8kxBzz9Fu1F',
  '1dy-eTkUqKLdAi5NIWFZsVjMvIE6QjlMy',
  '1TBY5hHbgcnS1kPgCYyIu_17nXuIJILed',
  '1rWemivLYFgoVC7M3eCECY3m71c9NuXpO',
  '1HbyE5-wcdrCtXLNKX5ikawylmiNjLNKa',
  '1EkT1-zC_5tR-IHvksoJ38t2cmoQPlSi4',
  '1Vc14Hr5jZNwS5SZsIObhZD9zwLRb7bPu',
  '1KsxgtcfmBTJlleg4q9TEBZqo7CAyT7Dz',
  '1bQOsNX330F4fXcBW9Gg0kdFj4m7jlCXI',
  '1ruFTlgEKW2hlM8JDmCQfDrfPwnxEdYBH',
  '1eqd9S-aullovaLsT1a8QdcHYq95sbDiq',
  '1du8mN9hbBHP0k7dJkj4dPdo8dhdieVWa',
  '153y0AYozUIW1jOwFBtfglxL0ugTwIItc',
  '18hVYCBh6aRMftOQ-bK20opsweeTk9Nyu',
  '1b-PWPuRZZ_bRiOx8ebQ9p-DLemohPNnJ',
  '1xcIDIQyuLW45YZW-IUK8IexOYOT528Pm',
  '1xJp8J1bKFeWtzxkfMLMBKmI_DGhy8_rf',
  '1VANL2HYsLS-txXyuzU-9OSEAQDF3EPAh',
  '1flZwosKE8q_wMn8EzkCcOB9L8vAZrN5C',
  '1xeZGcG779DKt4VHBsI56QMyvFYHJHErS',
  '1xtOijE-dnjfiCPFCIIsg51NUz_bP1pui',
  '14vRdZTReQeduLnAd2cx8OfXTVTLQTlWL',
  '1t3Zq2-KZ6v97i5LqGZRZD47G7JlZaZBW',
  '1i21quDYRZwPKmNdKmvZxkf3ANdNQjweI',
  '1R8wA9KyF82UrdSUZfKmybAObcm-1MzFx',
  '1rAZ90IUjf7D8Q-h27c2S0-j9TPCcobRi',
  '1M8AxbXGkYoh_DLM7UjYI1hPYpNb_fFSh',
  '1Gj6tvZuDr_wNmIiR1AwTHKp07xtm_u29',
  '1h5pdxZFzLjgHkxAkB4a9gCqPe0ovBZ5V',
  '1s0544js_cg0ikAGdSjudymjJCWDWpJ7i',
  '1q2l91ekrF28qFo2c5vObwv1KMORFLM2o',
  '1oM-6GT2BjJn_hvXzLGJsb_-M--elGVKL',
  '1Ps--obSZf3bxM3wkgos4_Tey6rsej5NC',
  '16CxySBniobiAzbJt8CEdAckx_v6UP0fk',
  '1oCYazzPL8wncz1nrw_53dADv8N0fal4a',
  '1e8eRQgDM1MqUilWCyTCx2zG4Iva-clnx',
  '1_yaMY1jBhwcEPaqAKkW7lZc0wHhJ4n2T',
  '1IxmNNoLsxKJ0x-8ke8q_qU4r4zDQ8QTZ',
  '1VR-CZwissYusvbFibwtp_Q7UlGP0euIA',
  '1JxG8m5cocj20e7vUPQ2AJGr7Mr_jSTqk',
  '1GxRI7fsJDHN4ignwGBVgV4B4UyRe-EDz',
  '1oYTaFVemNEygbptbw8pbZJfOBdCTtr5W',
  '1vNAAnB2tcux4bNeQHjFg1kRjUNN1rWBG',
  '11Sm6-awaT73rJWY0eAfC6DoiHEewrVPd',
  '1jSXztOgweCh8h8tVrFyRMB6MF1gORiyl',
  '13zX6TzDjb8HxAJozyF_RbP1UYUpiU2hA',
  '1DvoY602hgY5IBCEfO6n0xDk7RNewqr8h',
  '1xDdJvD8xryBgl1nao-bNi2B0dcmbpgjb',
  '1Zquw1a-ysOJMUiEeKNzpnUy9pA8cb6om',
  '17l5mD2wu72mpvZG8x5wWrtI5Qkw4th0V',
  '1y-dEjZlIMkIHD0SYN5cGkARsQCPTJmxK',
  '14H4lrWvE-4nJVQxTvMNMD-IVxqi-oTze',
  '1carcFjf0AQwSqh-8gkYKW5UYIdGk3U82',
  '14lGhqZMa8iLRKJgHojeLBF6SiQV3uQrZ',
  '1mGMLvPg6u8Zge_Gb0lzMUqaPnrhmbdQ1',
  '1dcOHjzLCmNmFRvE_C2KNg_d6R78o27BR',
  '1MPJJfoHDHhcp6KWzE3oSbEDgVALNIv7x',
  '1C6Q3HR0ImpJkzIr0uyCXR763ht_BpkZo',
  '1X-N4fGP1Rr2RFdg8uV9W4lI-B7798Jl2',
  '1ZZgyneBfmeEZa67XhtzXb82MKNT4X5Fx',
  '1MnSGOyUl_d7PVRsVcPiR_e8kr4vOv81n',
  '11010XOovSpmF54S5UKJbN_cHfatV_AGz',
  '1IPD0tdlVVg5IGdzT33Q8z3zagS9ASGgK',
  '18esRHZ3GLK40LQTunhYGHkTEIE2sebx6',
  '1AbzUc9wZgNQ7WwNccvlycSP3X9fnX4fX',
  '1pAaAK7Kv6PB0Za6dJwokE6JIe7dr4_wI',
  '1VNh9ujHdSz4SKm8DI_hLv9BiUHNOsEAN',
  '13hVdsxjjgj5GAK26R7ZtZFak_F0sevHf',
  '1bDoZJMSp8jRNcuHQ37rsTAMhnXRnagnk',
  '1952T9ksUeJC-532h8UdDqqsZi9lK031y',
  '1bPX-4wptbqonQuAzOfNtctFjMYVk7Gr1',
  '1V5B139kpKoAyaVdBaRLIHAxJ9i07ypIA',
  '17NKsD-Fh-iIQFXoz_5aBiuAqyrDfRsdN',
  '1HP5VrDJke56L7lc2lJJ1y1ziVxXkOi-o',
  '1j201Sp0eaDyIQxIKvF_HznNK9Yi-V8It',
  '1cEKfSQwmid4EgrgBIykvvMJBBh5nC_zS',
  '1YgRM3dW_OZ7fhFKRUnFmpxPaKz6c4WPP',
  '1ta1PWeuCb2_Dqnnd2dnQBmOg3kXgY2_E',
  '1yKNY9dP96TwPO7OKnO_VOlc3-v-ORXS-',
  '1e_1bfeRDFj0WY673SmdrcbtNXcqWtfdS',
  '11JPM8jbyHY68R6_uNPWwV5jDi5ej-mig',
  '1CQw5-58F4xGTzayBQu0NAFUwn479hMLp',
  '109e3sNmNMy8jhEFxYwGgrltK6GHHC6CJ',
  '12FRNWNnzfKyrCjzbFnzLFP0J-9HHF8xV',
  '1mzP2xc9-rr92Gi6GjMvc7Cdu31JbK9US',
  '1CoRWF3pan0BBZUsPVJSCUgZepzBL-cYH',
  '1J0-ia4wPb7Qf9VNoUTn7SS8aoQ2HFB_l',
  '1MzKRwjpoW7un0KfIJjotLgRMSzolX3IT',
  '1oS7vkmOnMt_ANyTFS27wv58LK-Jy_37q',
  '1MiGyYsC_8q2DJL2WSjTGDnAl1Qxw5Mpz',
  '1gbsYxVXLK2ZtGkwPqbsr9kuWyETkjVEh',
  '1T4mOyeVmKIkPd-F1wCVUMhsfgAc8Zejq',
  '1KveblxDmrZBe-1TgGM_aesFcDV5LZQlN',
  '1dcLj449wZeVqW6LVyZlqAFi8SwnOsV13',
  '1J1SHXHoIcthfhEXukm6R0V5NC3ibAw4A',
  '1gre6-_bgpLG652CO9tzQSwXmUgiL61fo',
  '1X9v7osNLyJjaDDGdtx9WzNy9ADSY0WWV',
  '1niHUvMxSO5QGxD6VFaaUfjs6qUz8qpPJ',
  '1Ztg5h0PKQlOuIWBMEDGIIYnR9PLvF6Jn',
  '1hWWdkkVcD4RBkKx6muokN-eDHrVyOBks',
  '1jn_NU0OMWgQUKOY3-7X9G56TAx_dYXJN',
  '1nfyCzwr7iVB92cIGva8_rWzL8IxEmPtD',
  '15HFSh092PXOvhZtdOin2PYslShDgp15Z',
  '1j1ITMV_7KxSnOcJTnu7vE0H8SBdgu989',
  '1QX98UnK2IfQ7aVkSTPX98ZaW7ldorpIg',
  '1s_I8fGBTezPkr0jVu7i3-K5XYjfTdhK7',
  '1MoWzdVr6dECOu3wZqkoVSvEC1gE5LhSw',
  '1XAGEbjnoQXvSSLMv087Ig5Epcb2cBsEw',
  '1ct2Vts-YeHUVa5cE1qLUorHF9gqMbFc4',
  '1F-gxNusGievnYWZZGYdRocIa-gkjNz0h',
  '1SyfIFHOtkDfk10ka8TIVM44V4lXb_phk',
  '1j_F3pMZbu8rZFAc_SQ51ydKzOci5gmEh',
  '1kK4MbVp2ySknMMiml90k-bRJBEU0cDAK',
  '1ZiF_qSH08qLv_f99S5NHf3En46LGzVKI',
  '10NYS1TqzjAy6Vyf2p5USvgpD9gkW5HTf',
  '1C0G7KAA7-d1Ch6hB8CtF7kS_KPr79jiy',
  '1tH5hN6qosIGkiw4NZ3gXTlIpGIfqq2wW',
  '10hKZfCB65hB8z6XAi0BJ_U6CwnU_VucK',
  '1yl0M3HGBcuGr1wOgXPG4lywLLX1WDo9s',
  '1HjTvcbMjjHF8Qp_10FP34J1W3u9jt3zW',
  '1zKKaViSqL3j_zN5eJiaCwduK-590DfBq',
  '1B3w755en8xslfY0KusA2VrOk3Kib7OnV',
  '1yM7ZzDtsjgTgTLxNrRGdw7UccH9aoCTI',
  '1Kt9a0he_bAXcl2I-rF4u0AlJBIkhSedD',
  '1PKNRilJororn2fxDX-u7W9tfYO3Gz_rD',
  '1FjsFnjMXOQoNsbNk6xgdpakwiQxpu7ew',
  '1HTXxQtrTVyiQIYYDQLUVvbwEp7jlGcFD',
  '1mABIZ_K_q4_sx-I-QgBfpQo6zG-wL74Y',
  '1BBCnwenZ6ZEvXfT2KlG5vooeicq4Rh4M',
  '1jMnsEBjMJ3VW2S3fU9vGiWeGX16b8CYX',
  '1kc4jy3PF4gJCxMZ-JNmooOxcrXPBd6_y',
  '1CzkpEaXnjpPA6lqsWhuPvBnciXSeoYqE',
  '1kUaSB_IIyJSrPTPSfjwpF2gCnIYt0Ay5',
  '188DfjlP_0TzaGMcJ3-nXFgKg6U3rBYsB',
  '15G3jDgeedNc1ljgWyTnnAVXrVoVa2MVC',
  '1ROET636U17bpSolzcNXvfgn-jyqoj4Bf',
  '1DhNjhjQBo5mmh-D3LH6ryENfI37NiIvN',
  '1mfg7IcabzRDyP24VwWlgLlotZGPmAmQo',
  '1KlLXmxhkNsxbWwNfuEmG6lT0gt7DULpT',
  '1tKYtowHRjqhvLQiKHl4XB3seNQsdfthS',
  '1PaxkS3c1GVK5-WphhAd-ORtQoz3mdhKv',
  '1-3dtyhS98o4XBGYPGy_CILsIYQk1dtTU',
  '1lKcLfY58cBRI7kX1lKhOCHuqq3ZjvHri',
  '1oahyVEjBErjWKbABVqzEMlFAXkz03jbi',
  '1IsghaDx6Sl6wK1zzgrBR65iOrZYymTH8',
  '1u3XUNA8mHWhAsE_qCGgt83KruNF-raoZ',
  '1CGrXMPB0dJ9BuWQYWSmJvwU3kIcemRZU',
  '1cggMb3lsGVmNC9e410HkXzYqWZZGjo7e',
  '1tRGCBThZJZOFaHUGjt_TfwU5RBDmJpX5',
  '1jfXHhatsp78cu9xPnI_EL26oEZKS9N0j',
  '1GPpp4G2gCI6xqzXOL_O58qzZT-g5W8d2',
  '1MORc3SSTS6dDQdC4X3xpftXRdL38xvt_',
  '1Z_7x5y6oqpcAxMegNrOYneQiRB1lVYwk',
  '1U2FNvX9Fb7oxiEOvcJvHmnCydgXtJtNA',
  '1ZxRsblOudrVvpQhGg3bmbJjJQOaH6cql',
  '1ANHxS7BZJFgzWO-kP608Upyti7o8QLm5',
  '1rm22DaRkMThwargnaUKUcMB63vh504UY',
  '1CmVKXEur6fM6Cs7XKeWMklDRLqLEkqFa',
  '1_zQon-wYZnK369kEAem3g7maArTr1pHA',
  '1nwe0sYMj0kWqDkxFwFRC6t2n_q9kqRuw',
  '1YqtJLbAirMn-gPxWDnSM9y8I_YwRfglE',
  '1O_rrJk8yI4fAXP5HrDLmguTP6rbDzEyk',
  '1JBxMbrpfaR-WYQNgfoie83AQlEEdodJV',
  '1LGj9o5B7sFRZJ7zjjbPOTxOz1-aFJF6d',
  '1eDSHGieuo6iKLD8gzQhoDfOukiCO2PuI',
  '1MFEREJKffukbaQl400hjeqUywNo10-eW',
  '1amuWn4PjZjAX9dRUXMLzJD8Og9ohy03_',
  '1GF1LmsIsaDbqitfb-JPicQ6W5nxqoG8c',
  '1BHEuyHuOXDVDcmLTJXWXeaOv8SZCeXul',
  '18Q1IoJFjowxCw4kE7YUmqUhoEQviCz5X',
  '1KXtzM-X6u0metwjucg_88ESaOb2dvKbL',
  '1oxnF1Q12FL9kJV858bIpn4SQ4YZ3Oz2j',
  '1WMEgVoRihEPq_e5uNEGKvDwkZ2zDIB51',
  '1DRnt3BJosPbwtU3I-CgvDt85rtZ2DrSY',
  '1aHhkE6AK-mQ6zDN9F9zkz4rX2fDNusAc',
  '1BWJTyXvRiepzJnNeCinLpBOe8FnvCcNO',
  '1Xg_7v4cbdBDtWyhMUCGH4L0SI_d2CBHU',
  '1CX3ruWxykow4YrOTnGoxRTlJ2VCeCMYd',
  '12to3dxLRtZIZekbem0ie0xTcVqabnw98',
  '1dfTL1BsbHOkwBrBWIs74PwobjrQhyubM',
  '1tLxV0UEjVH4MUYFHnAbtFwY_2Mldx2TQ',
  '1H_B86jKLeManJi7VROS6umbLFh0NeLQZ',
  '1e_Rq8ImU_gYuHAtslOnClURPfckdW8BN',
  '1M0PLA282Tpm27tCqR0MU4e74SRmFSLy4',
  '1hh9eCMgRPrTP5C7tO-dmSP_ItEIj6zdY',
  '1TafMMcK30tT4ZrwBlxWsUM53Mi117n5S',
  '1uVTFccKMe-8Y8wu6I5SFkPZG795f1UJk',
  '1qTeB-yp639MuIJH_KgyO7aDCW-TJ8Sn0',
  '18HvON99NpaYozGux5S1LVblaUDBSWhl-',
  '1sfumz8uftz_4kaPJE955yHR2N2vRm5wy',
  '1VyPW2p6Jlhc8PBOygS2E0V9Tws15pQ1O',
  '1OeVP__xEvqJu6tbkpGsh4b4ByR-H4mb7',
  '1chjT79FFQLYScGmyvyaBYwewNYWDG-AF',
  '15BcjE7QQHX0slL-T8afPTSw86nIMG4J8',
  '1IKI5aiion8CAkPwZcAMxF0OmMMxybjYc',
  '12-9DiI8rmrrRIKauMIMY3e3WDfRN2lVH',
  '1LKNAd4I37ZxAvUs2x2U8n7SLcuWUrXOk',
  '18WVfFn4Mwy7m_mGwEawe4lRlIjina63r',
  '128sJOs3b6UdDio1oWzJF6irbL63O5DPb',
  '1Wj1o-I4_KChh4ZwveU6gObT4kk7DboHb',
  '1l3sValDXImE9SeOs_vGY49S-OfQ3jD8p',
  '1MfD-yxhX30Az9hloLxGkQX5Ljw26o4by',
  '1vTOCEk9wTp9P3HzcCOZolNJ2Incbfrrv',
  '1IIuE7m8N4vpVAT9L1YmAib3Yv4t_y-NE',
  '1x4y7SPTd9dqLZAicSwLMtlMmARRsbdeZ',
  '13l7dugEqAdpqoj23f5c2GmGzj4xToRcN',
  '1S6DOk0jFsT02zKmwCV7Lzh1nEVjlq10e',
  '16VwfTeA1ecVsG9iB2tuGHN2uqbHiHTzc',
  '1Ic3QQqroN3P8gZwQ4FAbJt0gBNKanOFk',
  '1tZw2kvp3qlw90UjWTKXJHKKx3dSpoljd',
  '1boZT5rXtYY8XGWsXgNtZ3CdncZE26eUg',
  '1XfOjYUo2k0OlQhhm3RtFh3Ab8JjQca0U',
  '1y-rVPx32awdGBqMWeDdgpHPK-5csWiQc',
  '1P-9v-eA3-hUMKtWL9pDFwKRkLd0r9Yv1',
  '1lQOeKP_fgYp7XdjQmHA20ZMN_GMUcodi',
  '1uNU8vjGippjLiCPVSDnrW-wdkm5yMycj',
  '1bFqCMcneCts3j-YJtlWF62Kq58g2mLjv',
  '1c64srk8Eh_azEe2UJWBolQ8IeeWIGe-Z',
  '1nQTBG961go6VZIJpzt4SIbAuw5otVy34',
  '15_arFxEy8khNd-pAeIej3kXxL315cgYD',
  '1W343iEJnraoGvq6NcWzL0_YwMbs274YS',
  '13Efe4atjv1Vir-kdyNulER3oIopPG2Rp',
  '1bLK_xZ4mBqP4hpPQnECDtqGcEwL_XJzp',
  '1Vhcxq1wcxmTmhwcr8zFjqIvMd7i9lJrd',
  '1W6u1Oqo1q-VNXXNm-3U5xaTLPp8JoAUN',
  '14TZXPfrFLmJ-UBse7laCzHjiv0kAPSH-',
  '1GsPf6EosVJfxWTs54gtC1ntfu-J4Q57n',
  '1Yn9vj4uGNtEtv87xNCqvOoNMkCZPwxC0',
  '1ocSmVRnxGjtaTnURP3etJCe6TE9aQpOB',
  '1VMrG44MDspH0XhWF12vgoMu3MV0TbIZ4',
  '1-kUf6KyIVWcIC7wbS2ZlmbICJYKEHS_k',
  '1Fo6lhi_vf21hd3l_bHW5VlFrR93Fv-F5',
  '1Gk2iVEfGaBqrV47ID-68DwpBZYZOZfsb',
  '18RjZgXb5V8dNg-LhPgnPG_6ypENevN1y',
  '1GF97W-lkTd9OqGqL9qtFdBbF5qtxb11v',
  '1sIddfnW9kK_ALLo52GXANYDt8RzHgLI5',
  '1P_6AxX4JNm7hrKW8LIE49CAECJJ-IJAk',
  '19WHViEZAcaAODb3Rhpgwp8PdGy6XiZuB',
  '1WFy19jabNg6w3PeVWW9elHZzGPGj7Kdd',
  '11iQCfnXPVMJTIfKaP_XkK-MDC3wwz752',
  '1lA7_Xr-yk9SS3T-KjVQyvYNEvmZlXBsB',
  '1VScAg0WlJQaFCq8iiFECcFGdqtR70j8z',
  '1-zzLcUDua1lv2Jxc95RwCHBKsYgpxbzv',
  '1cxDgu93PbqDgypkf6ZH9pgGfvN-Cl_Lm',
  '1hIjIztnH54WI9_qC2CfcO3RkO5g7VwpK',
  '1f9P4DX8VOqt6BDE4gjB0N1k3TwspJUct',
  '1TNZWIh_Regmfsoxqe7vupNVA8E6uE7hO',
  '19sxFrfGexKDuW6i_04QKqPWBAl5EGpKU',
  '1TKvf4WL1zv8awmbjpWYr6vnWvkRDNbnl',
  '1xrg-OKuGGHzUp4fXVT633vdnCDQfd2KP',
  '1YJ3z_w6pBKd6_zJIViA9mea_6hG0BL0p',
  '1qaSeAFmLszqRhpaBp8j2yheV69_b-5iR',
  '1iQmQVY6Z4iMSWnBG-x76VIKFJ-ht6MA8',
  '1HUf6Dgw_5irGeMSSadpBVL2yIO26OTU-',
  '1oLSL4KNaZjvZO3rSMBjJSwFxMbUFE8xn',
  '13bd4r3NUDgMGzT516KloHfC8kd1saD_L',
  '1VcFi3ZyumFBO00hjzOjDVpRErZS8n7tt',
  '15xSjkH1Y5s54eR-d9AzuDtZ8FEPrq0mP',
  '1xpR__zgEP7Ty8G1o-jiWsRqZdxirVD6L',
  '1M_wYZFYmHPCkP8NXe8xIRpPAI0dVjOg0',
  '1AmHKlG9n8FW1ZRZe7RXVBZJ4ipH5s3J_',
  '1ELMSCmIMlFd8Eehr7Z6h-Qu1EfRApuGq',
  '162VE4ZZaHN_yxmcpwY88Tzk7pnkxrRCk',
  '12H4v-fpfTpAZ1OVMQWJvSraSipD9RhOW',
  '1q9CRaAfbTOWXaLhBT9TutYMJxdtU_y-z',
  '1pjLUgiSU5QU8De4isvhKZyAbZOlvVQiM',
  '1TBFFkEnMUrNXu8N4AbGRX53IkUXJhpnI',
  '1ckjhBfIcRwo9gkBYgtPEe2nPAjlva6Po',
  '1QFSLGgBcHnBN5fAEgr0nT9S5W8fnM1KO',
  '1uyoG_SC6_-APYNFACj5SFo4BXS8GJH6g',
  '1PbAXj0m4iWqcFUnfgrEaQOxKZxkkZoa8',
  '1I1ptFxhKOvqnb13V3E3watd2qE0-jkmP',
  '162A5XskUj9Un0nXAjDNsvdRMpLXanxfm',
  '1dlmPeJqqtvkZzF6a7qP6EUzc9E2jueQF',
  '107xLKEBGjWSV8UeO0ZwbdE5nbRDMueMg',
  '1JTT75w_Dk6_FQLLQ4TdlgqRGhyu4XIhI',
  '1WFkE6klHy5k5aW4V4TUpj8t7MtH4GRaz',
  '13ogl6NLm42kbJDXKGTILPBhUZwagOUxf',
  '1nP4Np8y6idK4cn-MV1hDw4-0hGm_M6ud',
  '1NTUAds-hvznK59drP5lHntouCNUWh-sb',
  '1mwkoKoikZFBgB8m4Y0Rjj22H8G3lTARm',
  '19gzAj0yMA_MEvJ38B_pV-6NVfgsmUQe0',
  '1USZGTgAFTSkT1UypjBSeMThcRFqSJDR4',
  '19CGRgcK_IjvQPTPk4pHlblFhMI1j39Cp',
  '1bTq9iFq-9VusObxl79AVmVf-D542AGkR',
  '1dUrOmkqaVGNM4GPnVJvBFBeMOW6PX7n9',
  '1kdkkzMRXYIW_r2ICjPO4cmKtYjlItWNV',
  '1XTrS6fC8yROUyb_SI6phr8DcsS3jLGJx',
  '14cUm6a-5MMG7vR-Pcwcqsix5zmeB-eWP',
  '1znuFhrl8tEqOy79NXzpgdm5XEoXt_O_-',
  '12TZPBqiqF6dkPt8iiv5IjAnBU4ARZ5mm',
  '1VYFLmYcz0l2w2dq0ido6Z5sdYoYRgJf4',
  '13lClh5W2Amk23YspHtL6Vdk3rFZpR9cf',
  '1SE4ICzeQTy3YPlrkegkboznr5PWsza85',
  '15b5sxvwA80dx7pp00kkPVhywo4OSvBmb',
  '1qYewuC8N8g5Unl3HbkyqBbwV9n90QZ14',
  '10bDyuk7efKhLhF8Vt5680pVG5JUUz2kT',
  '1FyYg1JEHKI_SNBQj2RXnUJogfQ00wzG7',
  '1LOBH1F-h8CZoUPswyEoxbJ19j1KVxqSL',
  '1fDI71kzovT5mAd-aMpsH1xufDDuRfZHx',
  '1ZjmGTtKUJKEWcZNxO7lF00ZPlpCKHbp4',
  '1bivsKV3oZ9d53pOflNIiZmJrl0ARu3oc',
  '1obn6pKQwo5UZl3F-J2IxBjI8pQzO8Gia',
  '1Uxr8nTzgsUzonPAG0OytCAdF93xB_r9i',
  '18TJe6dVhi9Kc-otHx_F5TWnJIFaeILbc',
  '1yPSyA2QUjOtnzf7KBnrbvxwDXQWeuKyU',
  '1jl3Nq4mnWCzrK7EIX4dNeaKzdzW3yBBO',
  '1yQ-v5VIYLh1GfEgNl9ytYjppOmaC3gaU',
  '1iqF6cZXlaPqxCmZNsHg-wS184cMp7q-e',
  '147aGPr6Dqb3MZteb_7kTI_vmWVtUMDiO',
  '1NXnJrg6QDtJiR5Y4t1YfeSS336mMHYqV',
  '1WIeFl61e-0CCG5xpw922kga1z1JBLEzc',
  '19mNQ2YQkbhc7Np4vu2I4wGVSD6VMvRog',
  '1xHmOUuCB3hMydnyKtVY6FLmQ_K6mPxWA',
  '1TiHBrfXhAfAmfQsYsewqYkU5PUzBMHpa',
  '1eYFFqpPZLvduFgLJuavN0BNrXkdO1r-l',
  '179gZFSltHaEeqVLwoJSP23rNKmPsR4xm',
  '1_5DgWFSnuTCxv7--7II2VuKmo6WLBMg0',
  '1rtfVb9Pu5bnW60yyT-rSyLXsvbAZ7Ibf',
  '1-ZjIxMdtGw4xJDlExYzUnaFrVXyhJCi9',
  '12iFb1tX79JZsRsAAW-vEM13U39yiRQMW',
  '1QYrtZgi-CO4Ba1LWrvxb_qwOLRaTJJHd',
  '1G1Q1fTJsggdU4caMA0iLKZr-TrRsVqlv',
  '1wT1W-RMNBHWP5kzE_s7bx61jffgYYmlw',
  '1iTvw_pH1-8RPRqhjwGZ0uD6sIaVV-02n',
  '1HSDkZTNSxQlWhqg464ag51xR9Q3AG3CB',
  '1IHLdz3aA3WVw5pGyxaDTSPsVtP36vVjc',
  '1k0q5Osi1fz5-PBdH3PvkM8wRWdUr50yZ',
  '1sbnWeJXe-7MbrM_9npnvNh36XerDcufM',
  '1CNH7aegeQsx0RCHFdcDPs_atY63p1Vm6',
  '1Xn5Ccv3fWw9QjekoOhFp4ldzqtS1l35a',
  '17HmEEPbbZJLrOgDfMZY4GukZQxTv2CbX',
  '1KZaNAoVmVKGKIt339__Ufq7oQcEc6XYF',
  '1HeeypWaoSo-cEQ3EVxig1VdKjH84n6OK',
  '1U0KJ3bCf_R-zX3JbHB0JRQw85UkoI2-e',
  '1Gv76c8-LKdSVceVaF4JCei1oSg-K_ldX'
]

const selectedImage = ref(null)
const loadedImages = reactive({})

function onImageLoad(id) {
  loadedImages[id] = true
}

function getImageUrl(id) {
  return `https://lh3.googleusercontent.com/d/${id}`
}

function openLightbox(url) {
  selectedImage.value = url
}

function closeLightbox() {
  selectedImage.value = null
}
</script>

<template>
  <div class="page">
    <header class="gallery-header">
      <div class="container">
        <h1 class="gallery-title">Event Gallery</h1>
        <p class="gallery-subtitle">Relive the moments from the Ummah Twitter FC 2026 Match.</p>
      </div>
    </header>

    <main class="container gallery-main">
      <div class="gallery-grid">
        <div 
          v-for="id in imageIds" 
          :key="id" 
          class="gallery-item"
          @click="openLightbox(getImageUrl(id))"
        >
          <!-- Loader overlay -->
          <div v-if="!loadedImages[id]" class="image-loader">
            <svg class="spinner" width="32" height="32" viewBox="0 0 16 16" fill="none" style="animation: spin 1s linear infinite; color: #D4AF37;">
              <circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="2" opacity="0.25"/>
              <path d="M8 2a6 6 0 0 1 6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </div>

          <img 
            :src="getImageUrl(id)" 
            loading="lazy" 
            alt="Event moment" 
            class="gallery-img" 
            @load="onImageLoad(id)"
            :style="{ opacity: loadedImages[id] ? 1 : 0 }"
          />
          <div class="overlay">
            <svg class="zoom-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"/>
              <line x1="21" y1="21" x2="16.65" y2="16.65"/>
              <line x1="11" y1="8" x2="11" y2="14"/>
              <line x1="8" y1="11" x2="14" y2="11"/>
            </svg>
          </div>
        </div>
      </div>
      
      <div style="text-align: center; margin-top: 3rem;">
        <a href="https://drive.google.com/drive/folders/1KMVb7lrMoKbD7w0u86yI0bwiwEYwTcF-?usp=sharing" target="_blank" rel="noopener noreferrer" class="btn-external btn-pulse-gold">
          🔥 Unlock 100+ Exclusive Match Photos and Videos!
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 1rem; height: 1rem; margin-left: 0.5rem;">
            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
            <polyline points="15 3 21 3 21 9"/>
            <line x1="10" x2="21" y1="14" y2="3"/>
          </svg>
        </a>
      </div>
    </main>

    <!-- Lightbox Modal -->
    <transition name="fade">
      <div v-if="selectedImage" class="lightbox" @click="closeLightbox">
        <button class="lightbox-close" @click="closeLightbox" aria-label="Close image">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="18" y1="6" x2="6" y2="18"/>
            <line x1="6" y1="6" x2="18" y2="18"/>
          </svg>
        </button>
        <img :src="selectedImage" alt="Expanded event moment" class="lightbox-img" @click.stop />
      </div>
    </transition>
  </div>
</template>

<style scoped>
.page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #052014;
  color: #F8FAFC;
  padding-top: 90px;
}

.gallery-header {
  padding: 4rem 1.5rem;
  text-align: center;
  border-bottom: 1px solid #27523d;
  background: linear-gradient(to bottom, rgba(39, 82, 61, 0.1), transparent);
}

.gallery-title {
  font-size: 3rem;
  font-weight: 900;
  margin-bottom: 1rem;
  color: #FFFFFF;
}

.gallery-subtitle {
  font-size: 1.125rem;
  color: rgba(248, 250, 252, 0.8);
  max-width: 600px;
  margin: 0 auto;
}

.gallery-main {
  padding: 3rem 1.5rem 5rem;
  flex: 1;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  max-width: 1200px;
  margin: 0 auto;
}

.gallery-item {
  position: relative;
  aspect-ratio: 4 / 3;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  background-color: rgba(39, 82, 61, 0.3);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.gallery-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
}

.gallery-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.gallery-item:hover .gallery-img {
  transform: scale(1.05);
}

.overlay {
  position: absolute;
  inset: 0;
  background: rgba(5, 32, 20, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.gallery-item:hover .overlay {
  opacity: 1;
}

.zoom-icon {
  width: 48px;
  height: 48px;
  color: #D4AF37;
  transform: scale(0.8);
  transition: transform 0.3s ease;
}

.gallery-item:hover .zoom-icon {
  transform: scale(1);
}

.image-loader {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(39, 82, 61, 0.1);
}

.btn-external {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #D4AF37 0%, #b8901b 100%);
  color: #052014;
  padding: 1rem 2rem;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 800;
  font-size: 1.125rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4);
  transition: all 0.3s ease;
}

.btn-external:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(212, 175, 55, 0.6);
  background: linear-gradient(135deg, #e6c55c 0%, #D4AF37 100%);
  color: #000000;
}

.btn-pulse-gold {
  animation: pulse-gold 2s infinite;
}

@keyframes pulse-gold {
  0% { box-shadow: 0 0 0 0 rgba(212, 175, 55, 0.7); }
  70% { box-shadow: 0 0 0 15px rgba(212, 175, 55, 0); }
  100% { box-shadow: 0 0 0 0 rgba(212, 175, 55, 0); }
}

/* Lightbox styles */
.lightbox {
  position: fixed;
  inset: 0;
  z-index: 9999;
  background: rgba(0, 0, 0, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  backdrop-filter: blur(8px);
}

.lightbox-img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  border-radius: 8px;
  box-shadow: 0 0 40px rgba(0, 0, 0, 0.5);
}

.lightbox-close {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: #fff;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.2s;
  z-index: 10000;
}

.lightbox-close:hover {
  background: rgba(255, 255, 255, 0.2);
}

.lightbox-close svg {
  width: 24px;
  height: 24px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
</style>
