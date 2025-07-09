# import requests
from bs4 import BeautifulSoup
# from urllib.parse import urlencode

# def hit_base_url(session):

#     url = "https://www.linkedin.com/checkpoint/lg/sign-in-another-account"

#     payload = {}
#     headers = {
#     'Host': 'www.linkedin.com',
#     'Sec-Ch-Ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
#     'Sec-Ch-Ua-Mobile': '?0',
#     'Sec-Ch-Ua-Platform': '"Linux"',
#     'Accept-Language': 'en-GB,en;q=0.9',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-User': '?1',
#     'Sec-Fetch-Dest': 'document',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Priority': 'u=0, i',
#     'Connection': 'keep-alive',
#     }

#     response = session.get(url, headers=headers, data=payload)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     sid_string_val = soup.find('input', {"name": "sIdString"}).get("value")
#     csrf_token_val = soup.find('input', {"name": "csrfToken"}).get("value")
#     login_csrf_param_val = soup.find('input', {"name": "loginCsrfParam"}).get("value")

#     return sid_string_val, csrf_token_val, login_csrf_param_val

# def perform_login_action(session, sid_string_val, csrf_token_val, login_csrf_param_val):

#     url = "https://www.linkedin.com/checkpoint/lg/login-submit"

#     payload = "csrfToken=ajax%3A3504175982551558972&session_key=official.prithidevghosh%40gmail.com&ac=0&loginFailureCount=0&sIdString=f9242bb5-9d0d-4fbc-af6e-0d5688a6cadd&pkSupported=true&parentPageKey=d_checkpoint_lg_consumerLogin&pageInstance=urn%3Ali%3Apage%3Acheckpoint_lg_sign_in_with_another_account%3BHo9bUFtNS2iv6%2BDbmjpH1g%3D%3D&trk=&authUUID=&session_redirect=&loginCsrfParam=0fdb8488-af79-4116-8c70-a6a8927a9565&fp_data=default&apfc=%7B%22df%22%3A%7B%22a%22%3A%22VFjY5AiYlYuNWJaTdNFOew%3D%3D%22%2C%22b%22%3A%22bskIc1rQO177RUMjLF%2BTstdHlNbFq8XDdCF8j4ob1QNDfzcqP7QzLWHJBftIsOoTbv3mBv9ZYzbyg5iXhOOx7%2BYA3L49D4fkkPWGh2AVh684mvpRQgBxKZisE0nwrfJ5eAAV72MksKZHAjQmWCwF95nqxg0uzXA%2FG8aQL7RSNcniZgRc3eADFVLlXUfqVA6Yji4Ow5S4TCvVPrV7fpUnEG1a%2BAppPLvl8Y8cMw9ViriH1ReULyXYU2MUedCuUX%2BNT57Nb9bxXNSybI6XUOz98hZPt576r%2B8bQQ0yej%2BaC%2Bfz1QDaGtsKk%2F4BvlXe1xdyc%2FOXb7KOrTp3JlwaRabI4A%3D%3D%22%2C%22c%22%3A%22x%2BleLMn2bZVNKYWQ%2Bb4YH1PIAxIfhKvGzlFnW%2FAZmGP9AJr2q%2BmdooBIDkeFvK01w%2FwWDxrdYEuq36Nyafuq81oGn564wXxp9TU8F8AEPxhK0%2FNsA1sin9eOaKi0f%2FRABYSEu9Iqn5FA0W93m66uh%2B5TO%2BMOw8ZZa5FHxI3QDOM3P5z2T%2F6K9kzzY2r0ohKFoM3EjSSL7512BEuNDD9TkF4DOk%2BcRNE2213q6TRN6gEr85htGvXYI5%2BA8xn0CX8wTmGZ72U2Kf4f2TFU2rVdjo941evdfPiWY6Gt34kgBJM3xnKf3rCbj35DP1uaeJ834yW3xDzhOtLZ%2BNwenHaB46zJ9LOXdnJ6xJ%2B2ftJ7cSPT1g5MK49NRhfuG27huHFgKg3iGweV176DfMEcTbt96smGmrxyc5JI%2BeuCdopxOh78X%2FwYnBsRlDiRlimW%2BHFyoGCjL3isxr5r4u%2FS9bdCStP0kocnZLnRW8Gq8oM5NYxigANCjgZsKbahhhXFNL37WKDAUzMEetdk2Nf9jNFCB1bc8C13tTa%2FKA68aMpkBp4ExKG5BxOfUqgw43lVqpppGipmRvI0KXqGd8GrAwfBhAOT5rCchx2vhExmZccIqBXt8FJOi8exhBglVycEEJEdyYOidYjkUg0%2FZtf5m8xnnMvDCUoxXTNFN8ziV%2FXW2DUXuG%2FvHup8Fgf%2Fya7FCLFX%2Fx2eCrMFCxxgIXF1oWBMba%2BFj73mx6Db7PLrKBTiNcZszU5Phqqo4WYnNuqXJKZFWrmeEvRrQ%2FYmJy8SdlTPYtyd%2Bdmbr%2Ftwh5pjVubOBntu02Hw2pwlerdsL8hHOsoOAhXGQDTz0uJ3Nox7XR67vFFG%2FzCaFEbyG6c3rypl4lE1BAKrDsLDgYilMYn1lNi2pz5qRaqJlL5oZwLDscpYYy8yu%2BfmIvgj3tg5ep1wcnhbKovMQDLcFwo62u0lJESmzTWdvnNNO9VGxJvbgbF4SiVgNbQe6cLuNXkkYdd4u3OvIDWGslLr%2Fckng%2BfpYRYc1oYcWufQSmId%2Bggkf1Rq%2FG%2F1t80SjdiHDsBPHpVuE4ULGP9wcUgWyGBtvmSoNavrlQBpNyI3TKgZJBri5%2B1KNN2HzPaIC6BOSP1DsVjQWRjWN5E8%2F3l3SYgmpMWfbpvgVQMsVHExY2eEdCyyI6OXgvcNRaHPQaYmjIJRQ9RVu4eIvii0V1yCdIP49XmPwldTX7UwcSb0%2BvnVyTNmip6PkjZBrZbvtURdjhwn5gY6YuCNEcuXGsCgreXCpRz7LlLltvWgcPPF%2FYeqMn4A8iOS0G8wZ8CZQ0OjydCmQL5L3ymzR4CcOu67H4Tl%2BHZl8bZ7Pt5e4%2Boe8nS3nUs07F%2BGg45sexALPVEpE90xQm6%2FN%2BoUC2CteW2iKexq9V2FGI9GtHMXDKpouL16K%2FVPFr%2BVIT0aLhWFZ28pGdCMrWaRCy5ltIYMs413dVs80Uwn8rTYL6GDs9SjxMPgiYrUybErR0q9ouNjj00RJ2KvosUM3lbH%2Fn9NGp4Bqzd%2Bx%2B1wKHhfPn494fBLU9mrZlBq89pB0ElR5RMYx%2BBScP%2FLhdgebpd18J%2B2IBL1MIRHWSR2945R8gjmVfL9%2BnmfsGG00O0pFF53niCaN%2Fp7TiAFqFB50IXRFyAslGifD5mE0pWTsfAmZU%2BfP5bHlFoEK%2BTMZl2rQV%2F5Lg5oQlRG%2BcQEObzyIfLnL1BSsqpjagXcXx6is4cvUgEPSqa1IcYXesxIrvWCnui3IXnAnyNQ6IOQ9NnQcfM0i%2BN1XbcoiO6LJ2eVmE5ERblzKneRMr9RHNMnGBmBZV0EsA2aMqr5esQBd9%2Bjkzz0P86nnmOb12PtLmd3O3wN6wqXj4keF7acU1mLcxlSs3e6DjG6D188TS%2FEq8QtktfscjcNwsh8I%2BW2%2F183w01eMIqAB%2BfjcoICuvpndcTd%2BlQhO7UJywCRTT7nxq%2FS2SH7U64i8TX9n2NvDfBE7464ZETknEsR3iiXvx4r7g3VgyKnqADnj19e7ri7EO3aTEQVws7vUWN3B%2BGj3QZ3CUkbJWItaPLxM%2BXwrSl0MDpLYmzMBA0Orlna%2BnHPyEo1RtZahwWVr9ekLCUO2bDStef09SaStXjSSY6jBXnTdxg4PAZOzIZ7Z139sVl2q2W32ie%2F5tnpsbHi4GS%2FQjGgp57vSMJiqeBrv62quJUNhKmIwb2O2sxmakPHCVLtMfnX1kQ%2BNRuy3diGC9AaRkiOQ4z5yCCbJjzp%2FoJPS%2FvBCtwRCC%2BRiy%2Bc6VNkBBVXfC46eUG4Mz0ZPsQm6kJ92BVuu1pFOq3LOZTG4oc4HFJoEDy6OMNjWbrvozbz4v82SC669EAxWQlWsK6mbLhCyTsbS%2Bc0O%2FkxjxhubgVEcoVLlrQL5QOUhwQTS59wGSvlcz90Zd%2BHf5j8BlPchtVXs%2F%2BIUz5z%2F9BynyQwMvUl7qBUX87qzUBdk%2FNSbjtwSMhG0HCrZxV1Z0MfisYnPDbFRG5loZxuYKXsAPaZ30Vhcy3%2BAz%2Bf7iNLcSwW9pqcBa2NRE9hyYgOwEC9rBugVKilPHksrrclif1KpCyFflqJmGfh0pIGYfUe90zfj9YWpYde6W%2BZkQNo90m%2Fard4unSO7iAigJelN0uOmrht5llbXo7Ey6F8FveCiB0Rpz6RooIQ4gHJjRnu%2BfJxjHiqKarvvnc2tO%2BntB0ay7jfShO8O9tn%2BjyLZgranWn%2F7PUeHu3FZI9s0M6Jzxmpo%2FiGhCjv4Bt1oJRqDPNay4QtMWjMDeDr0goupWHBG5Kp9pLMX7Ww4YLuRqBmvDTiKd%2FrHuvk6xEglwmvnDRcAYUtBKW6oEPyEQhEXBjldV1%2BGBalEtWFd%2FTCP2PDibPlnRfeUnHkoCX5Nofxy4Leo5%2Fre6xRT77GM4AKM%2BnzZUNNpxY5n5AAhPR6Eqg0bS3bQ6hXNXreU%2B0WmU3oGitCIK%2BW4D5xhj9z2fTDcx7W7QB7HMt5XflTRFpcuwzfZRdPfGpN69Yy7I0R%2BMy%2B26xFZnY1o7NDKykYBT4kBLqdlbMc6OhEZKwSVs6d6DwYNxZt4j1xG3%2FZJiMApqedebdGSacpcya4ZmC6lzSEHQcBr4jkhbYwANA5PT1sXZ1IRxHR8xG%2Fw%2BV6Q%2BJJAsU0CYX4BqwUUWmsxjEHf%2Be1lb7mPZJpRrR%2BVLq3lX8VlLxEjMmZBQBFxT5wmWbObk9Ly%2BfSVIqe8d5QABV4RD59wIabU7NccRau7FE6oZgIPanCTHDDSajICD%2B9%2B4PKJhFC133eqzYwCa9zTZn0deFrQM3TJ29RoOADbL8mWs93fuiA6mM3E%2Fv0AXJkAcZN0jDESLDtzJEmr0hcNtHfsWhDEkoQmDYzQqxbZczT91J950GwIeuoDnqPqlTBIz%2Bjg7vx6a8QNsh14IliIqJJ9GikUtZHUqAUHv0XP5fyqS6JjphvwZ4woG3SzbW2Dg9TRrnjESzharNZiruY7DGXWEAU%2FD53ZjiZlCLU4Z6%2BJVgSRuY4JZ193Hb1ce6GUKA8lff7fR7QcB46bUfu9Qdjjmq8zUR0oRQBoo1qA1f6WtT0ZHJZ1FTZQxji%2Fb0EbY5goLvVs2V05cJoU9M5jxkt0WM5YqEnnXgVr1s3IemPnydNKPSU%2Fci4a83blE9eWQ0cnsG85jH1lW3YEQsK7Fira%2Bv7RvBPb%2Fwxuu7UkZ%2Fo1YaATwHAswvLrgtMn0qmc8QzAYNip9wK8qcXuLpae4MuRxJu0mZUFIJVtwXYaRxSAR6hHOgKW%2B6xWFwQkhfVWty1fB8CCtSmR4cjatT8T8U7yfxsAyYH0EmzXSpCbnoHoy8cGZyKdkUJEnDO8yxWKEjGAd1LvZdLshcdlNm3jlS8p3nWcTogw1zu%2FYCwGNryaWVx5TufQ3Cc5lKFW6TVz3lf1P1CQ87mF%2BHLy4IPNRnX2tnN4mZudztI2PxCjI%2Be51jbXqZxQApt1vCpuvDOxp880FJCNFfPyLevZB2uYwu6%2BpD6i8RqL2dli4JdnT128bZBjrBHKLa9WVsHT7U%2FZSsHKJVLPw3%2FfMzy2KTL2m%2FfA2SsPgZ5i8GWjyZSyA0BtZq3GBIcy4dEfxvsUYDDiEyRzjSicNtQwacEoF%2BvsOUNmT8UqAT3MYmoejJbow96URjJ%2BlhxjEuyLaBjum3bqFbTcM9chin88eb9DB%2BAMMqQsp1cz1Uc5zO47M7Bp51CTUsoNQjijqi%2FNyycG7cAzEY9XcJPWtv2sam6MCAGpweBii45mbf3FpWCJUCOYMWtZPzagk8iCfOnC0geas5ZiBn%2FXXaYZbEdG9%2Bt4osipfC5ZDZKUOpVWQw9LD0vlfKpoZ3nBJn3FYl7Ed3AdqF7YxS6fKCCler5ftCW76chQm%2BVVejE0WnPrADCi7UxOOHgkr5Xb%2FNY9C0%2FIkOJDjUu261ZpfklGpupCvYeAhhBEgUYdk2jyxFGWMu3e28%2BeuhuAFrEjQ2lIwQuwrj7JCKDyafJ%2FOOdmmK7DuiIJv8i4SAymVFdwGsTEau4maGNGYv8saQPbf1%2BfNd%2BAgycingICudmv%2BMFijmBgYGUM%2F6MBv9aG866Htx1F2wQPhs36NE%2FnyTzTMdsYIz3f1zBQSl7zwgNcwPhEse2hMPPcGuFUofYnJjd4PnWuZyjqlq7eVFlMLcVdgS88GWPrx1LvgzTtsYesvZwxs%2FPXDEqx5BayUt4SOpGVWjHmEXo4w6bVP4Uoc6z6Im5d9puHXjkMD3t9yymhKx3o9R7qMGajpdErMN9x07YcWeMHurtnAgqvYOcoCK1hmVHN4LeDyRikRlvkrMzMzSGoNnpLGQalag3nVLnGZ7LCurfUS8mI7KNpB0OloPMSdAMM5E93As24GIVkeJ%2B49cRd7W8uAUJADftpCJaTrao4t6EFI7vXgfA6AAMBQUsZPCnNW0KtV7%2BmzymGO1pb3%2BhM59T%2FiLtJBDFm2YzwVnR1PTK4xb9Hi5oBz1VAOVvjHbHqbEU02jTTQYdFflGaOxp7Ff%2BO%2FlTFj7ZLIsavfvl7%2F%2Bj8zyIR4pFzynXbGZGsRa8F%2FILTdUnhGSl8OUzJwJR1%2Bf7V9Zdku2%2BJ7Zqlgu2t5%2FBEddhxAL39TIHdN5OGD3kcnaYB5aSwBZwKBG4NjoJmHTF2B%2BI76lU%2B3kPNFLgQwlrk%2BhYO464rpJtDnV04PVydYp5Lk9Kk5NzlibpYk%2F0ymr5QpZ1YxNr68c%2F8yH%2B4%2BVYU%2BwkDVrU0c%2F0vDvPnLc683o0IRgDM5rGmHuPnh1kQp1NhvnFoP65ngvmUH7JjJSy%2BNSKACsZ3GX%2FKVQ144N8Mel821jILhl3ZTGxbFms3BKi3QI3H55jZFAZ8PgPJVhs7%2BJhGyL0j0%2FTqvPrcF6WWVyNkxAmVziR%2B%2Fl%2F1zomx1btWc4AOA6uOq7trsGMMWCkqSzfaIEPayJqwWbeRrMwI7Al%2BlOyP7Se6XaWZxgGmQlcGVvPuAFg1iR4x21x5D4StDwWeNg1KJKS7eekd36AeX2mPeW6JyrPjrQ4LD2K%2BSnJGGq1NLIwbMAwVPKZSTasGygUKY%2BI1nsd8s%2FbcumDAUg3mu5FoPwOLPOyP36Q4bz0QqNstSyJOC0c7DBlKBQMkz4qGnP8dwWveJPXy0evfR%2Fs3klIiwUvTutHxSwqoELNiLKRWGUVt3hSpBhUJ0KanUDjfyceTApx6OUoPKv05CJW4Qm%2FFoKqZtWdh6y1DOnpQTwp0mo27PJDJ4NcuTEKEYNBxGFxeDZGJMiwY5v2Rf7VxnARae%2BF0rN%2BAf5Z3b0MpoNOO6OIuovhKd1hh9Vnx6mQS37QrNFyy8Viqa%2FpPczjNAYC3JCqJ7wIvIaMHal92u%2FqXaBJixHz4Bzm0kiNgXOWwyn16w1FP7gR7GA6evq3ni%2BkKgdXm0wyHDOp1YxH05NFDaY7jHc7E%2F174MgBPwNnaq7CtqYOupeVjgKbkM%2BIgHpg3o2MyZh1f%2FDapkYoQDyjHALNcJND22XQysxGw57GGuRzFdmDMVLiHlPkCwc5ybUqpRpOhbPkDqyI3kO8iV%2FUeHG45UwIV1aJBU2w8HSPzVEnl0HdDA70Qq4LUKVt5lfoGsszoxmEAsKZ%2FlIisr%2F0F902phOu%2F93cnkXM3sYjn0D%2BryKFeAc%2FToagzsFxO95IjFmRz%2Bg572sPQ%2FtWtLfV27c89rmOnauVn8vyfiin%2FGvUI9v6fWIwy7w8ZzAQQezLnZfu3OmUQOwxh6WbCgToASEpxL9FfM69w1P8p0kCchwbGpGnpcwfdcKEYBKtIcvYRuzdX4aizSsrRzNY8%2FB4LrnfMU54QiyP6DEcVVNccOxUC18Mhgre0kO2%2BkcvKtYPmYx%2FLPrJ%2BAeUsM0PEgKg1LhCuUUTD9U4%2BLD9n28EMizyHD3fvKaKZ3Yxx0YgzFnWvjZsk3MJ0ZAOnWtZ%2F%2Bo9yzwZPbdVk0LkP0%2FDUVEHgCDTXiPRzhGzheN1AEGVB3McDGmaFmFXQrkM6jfUv6SmyOzSE8V%2FKvzCy3C32XOpMlJDmG9SPX%2F%2BcY4vCWirCe5CILU%2Bjfa88MK%2B%2FUtpo1sW6tGvnCP3ivvXKFPbYXP0IxbRidNPWu3Omj%2F%2FGrBUayrPk9CJDhwqwInDOeyZTNIOqzl8PfNWEJgXX5D1UKR6Q6EvzogfA5zbw%2Fe0%2BZRNRE7iY3XiQ%2BvrqLJ21n9r70WHk5xwMQU4bsjd6Aa0WudBeaStq0HFQEUgOv0XEiv11cVjdK1%2BeEJKXuS0W9RdGanbG2F1UztwSLhb4GQLUTPbF1lsavJ80s3S6KvEKA9bMAZHqNk0Z3l6O6rIrWyCKvfwbCstsG78Yf1Ypj%2FxbXxk%2BhlMGwwvApHHab5sVQ%2Bqf2nY7kmbc9F5RMpO2c04mKlGgYcUl8NF1uPk%2BsHj5EJXBjMKbIY2rRZ7JM1a7Frr7NCORSgcOBmdfyv6nRxv5tmHuKClcGYUY8YQQDbZfhkmTI8gjCZYW3QAilQnKS4iJMVxmNhIBUcx4KWQUZ7aTYXx5Q40wKzknxwVaYGXqq1FQzenbhHFl5vMbdVqCT81fD4LD6njGcf3T9qWqLIacbQDJbCCYakYo5hF3xrfZBmF75p9dg%2FNiI3yNNY0N4XrsTxdhhz4wj3GyDYdLU%2FIGUedl4F7n7FifNrdbRw6TaPXJaHtHQpkDJIDLRtIDZNaZavgnyvIfRTUvHWf6vA7LtZ4ljTFLPhf0X23MLqoOppImZubTqAvV1Iby5qvbNdXQHLMrIN3APmUpYQYuVSjUKSSuB%2Fs1waLodcxEdlxwJ3dxtFluJK13zelh9ibfmt%2Fb%2BrOA9Hq8ldxaERyFpOIvzn0CE9Utz1qwzJM0IIVeM2LxDo%2Fm70BvBKVjMIC7kLi6ZXZzudVxwFosLFS0QUJJTK7K%2FTDvL010IJSxehVpdEYRrBbgFm8o0TkVUQoVrU23U%2BvFoVx%2FaAQf1CkKImfupEjieH6nrn20yc7WcWULX9aH7FB%2BemDBiLPg6S1T4mkkQz9HNTN7GCD6FkIkhjjGEb8CYwTc203BclHRqSCt%2FbeGs9lwhlsevmmAV6wQUyRSk6i7%2F3ysnO5FS%2BpDVgPkXmh4LQkfuDCj8BMYTG7xdCiq73vOvNlq86oGcDeDR8uHOWBTV84DfDk7GSLglkO0sWN7M%2FC%2FHIm3gARM0y8%2BljU5D6wEvDfeq2fJw7%2F95rc0%2BuEqLJOiEp1vdnNnCwEf3xiy278YCTTnOL8ZD9WxhxTOBm2VtTDPc6L%2FMugziSVuqPDtbOxU2gHXUL%2FV7zF2MwsZG6ABuY764Umqn5UZRIWyIyKrbDk4iud%2Bp3nrzIPkWAjklah69eV8mJewThxLBXss0Fo5UB8bIc7ehBSHaxkrS6TccMWw9D5XNpmnYeTHVNff7NbW5bAaMW2BnkA%2FkHrwsizt77t7KnZp5XGePLbLmmywrvmy9P2iReUa8BclQ318nfx8Pkhf7fkMMeSbAsJIBBbgHyrrvjn83LKju3GT1tuR%2BVzVUwsNKjVsSTiBtZMi6vyW%2Fev1nyDngyB65YKzUPUxKJ3UfM8Z%2FREF17EaiLfWrxz3%2FZia270VhjywOP8r5IAX6DCKoea8TltKJ4Q0%2BegXCMgXM15TNHh2UK2CxoJGlNTsmTq%2BsL6J3WErFP44zOCuqaFLlbpcdtl2WCb0K3ixDHmCHZWE5lO%2FsDANCsa1wLk8gPbonTN8HdT1BzQg5dhWAIU4vmFSgKdKubkYy3JiTrzquJeBWuqFWIIqwvns08vSjtrOqBDe6qCxwR28eRlOKNNzxsPsRKuJuQgeIVn8sOgYJkfG%2Fy%2B3cTt3zYgrgzLe1K8veaGstLc3dY8LGCIobKOxLV1JwCIuBjFrvrhYBM6csyLCVMyDq1ezJZ0ivfRloT0bogFUTLIaxwCtwg8ph9LooSXWlJDVvDqEAl3yXN8ojZYsJjIL%2FMKqo9DWj2jtdc4ghJzXS4I4u0bRbuUUgMiJa41akDvMAelYOTtvX1w5ij48azMmkfWmCdwzrZhirVajxji7u%2FxH7orpqPhqbNUuRRcMMczL%2BLVKJ%2BG%2BpMLKmMi221rLRUT5CoBpEIVuBM9KiHSMCndhXxeCuX%2FPOHaojc9p%2FptVwr69jp2pb5Znv37o4POYvmrby96xCAR%2BqeAHy9f73jkHJIi1GeqQyujjDMuZ%2BFid7NMiupf0kYhIu7nzg24u52rr64qLfaPOVOshzxQ5GG6QH6T6zomnG%2FGv1S70PTU8MKEM4TcBmkhsRh86%2FSuwLMH5Bn%2FBl2j76fTU5JqRmMpLp%2FhQiWdIN%2FV8kKOkzQKSo4aZ5vx6QqS0eeb1QOky6WwYgalLt4Y%2FUiTAskxQd6B579tjyD1MyVoAS%2FxTVg5g%2Fckgvt0pf99isw1S6FQSKkxkEXRfB3Scxv5GDlGkFycE67D%2F3PAXtbg45CBEBi0cbNZHukYiSSe6DvnAsmBbbqbzR%2FRU9jYOuCZqPdgudX%2Bog9X8dGhxRA6Fx0%2FZ1uyLiavQcCV1p5Cc2OLomIkbD5bxf0ykya%2Bxk2H8b4v5rb7CaMLRyZkvNKs%2B8dheTqW%2FQ2IzjnLNxZJ7EoumNmcOISF6imUEPMrw2u6PVxCpRM0gsta3gzOYPFuOTavl1NWb%2FZu68DlFNvlWaMBJWj5qfdwa417xWgCG%2F9aXMBuQlsVcfR%2Fv%2F%2Bj95XQO5IfzHpD91mqjjCz8u5ZDqEEVZRU7t3tE11Xhzqxnq72AfmrGkok%2F%2FVu2xq%2Fjfuafr7ltpW6xhVHbO2Z4XqDssQRMmotZdFGMHMDQO7Lynum9s%2FBqqn8aoES9ADQuu3ecwEPgYOjgPg7teIpKGJ9t%2BO%2Fixh2vVvPHu%2BNbbxO7EElP2ykkkaBKjmKj%2BYW4A16rolCJ5re7ILfhL%2FW3rBs99xf4EHaEnTvMzSl6vNFk6nd3oU9YR%2BCwj1jziPzpnFn5ddQZOXHXnUEn5hfVv74Fk4J%2BbglVvbXXDEu8B8E888ddUqSYJROSLkWruHpzJOOgfydYp68PNLPIX7GJRYo2DMWIancV8QmnKJO6zr5P9R3RN39x9mZVQCHr4FlTIcexq5eHZ%2B%2BQUd5Z7TvuwsR3RlOUA%2BU7Ubjj77OcJtIkT9UUydgjhmougi68jmjWe4e6ZNCG4l864CtneXxyQ0dQAqvvA%3D%3D%22%2C%22d%22%3A0%2C%22e%22%3A2%7D%7D&_d=d&showGoogleOneTapLogin=true&showAppleLogin=true&showMicrosoftLogin=true&controlId=d_checkpoint_lg_consumerLogin-login_submit_button&session_password=Ghosh%4039039820"
#     payload = {
#         "csrfToken": csrf_token_val,
#         "session_key": "official.prithidevghosh@gmail.com",
#         "ac": "0",
#         "loginFailureCount": "0",
#         "sIdString": sid_string_val,
#         "pkSupported": "true",
#         "parentPageKey": "d_checkpoint_lg_consumerLogin",
#         "trk": "",
#         "authUUID": "",
#         "session_redirect": "",
#         "loginCsrfParam": login_csrf_param_val,
#         "fp_data": "default",
#         "_d": "d",
#         "showGoogleOneTapLogin": "true",
#         "showAppleLogin": "true",
#         "showMicrosoftLogin": "true",
#         "controlId": "d_checkpoint_lg_consumerLogin-login_submit_button",
#         "session_password": "Ghosh@39039820"
#         }
    
#     # payload = urlencode(payload)

#     headers = {
#     'Host': 'www.linkedin.com',
#     'Content-Length': '11316',
#     'Cache-Control': 'max-age=0',
#     'Sec-Ch-Ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
#     'Sec-Ch-Ua-Mobile': '?0',
#     'Sec-Ch-Ua-Platform': '"Linux"',
#     'Accept-Language': 'en-GB,en;q=0.9',
#     'Upgrade-Insecure-Requests': '1',
#     'Origin': 'https://www.linkedin.com',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-User': '?1',
#     'Sec-Fetch-Dest': 'document',
#     'Referer': 'https://www.linkedin.com/checkpoint/lg/sign-in-another-account',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Priority': 'u=0, i',
#     }

#     response = session.post(url, headers=headers, data=payload)
#     print(session.cookies)
#     # print(response.headers)
#     # print(response.cookies)
#     # set_cookie = response.headers.get("Set-Cookie")
#     # print(set_cookie)   




# def driver_login():
#     session = requests.Session()
#     sid_string_val, csrf_token_val, login_csrf_param_val = hit_base_url(session)
#     print(sid_string_val)
#     print(csrf_token_val)
#     print(login_csrf_param_val)
#     print(session.cookies)
#     perform_login_action(session, sid_string_val, csrf_token_val, login_csrf_param_val)

# driver_login()

# # https://www.linkedin.com/checkpoint/lg/sign-in-another-account

import requests

session = requests.Session()



url = "https://www.linkedin.com/checkpoint/lg/sign-in-another-account"

payload = {}
headers = {
'Host': 'www.linkedin.com',
'Sec-Ch-Ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
'Sec-Ch-Ua-Mobile': '?0',
'Sec-Ch-Ua-Platform': '"Linux"',
'Accept-Language': 'en-GB,en;q=0.9',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-User': '?1',
'Sec-Fetch-Dest': 'document',
'Accept-Encoding': 'gzip, deflate, br',
'Priority': 'u=0, i',
'Connection': 'keep-alive',
}

# response = session.get(url, headers=headers, data=payload)
# soup = BeautifulSoup(response.text, 'html.parser')
# sid_string_val = soup.find('input', {"name": "sIdString"}).get("value")
# csrf_token_val = soup.find('input', {"name": "csrfToken"}).get("value")
# login_csrf_param_val = soup.find('input', {"name": "loginCsrfParam"}).get("value")


url = "https://www.linkedin.com/checkpoint/lg/login-submit"

payload = "csrfToken=ajax%3A1604855610149830055&session_key=official.prithidevghosh%40gmail.com&ac=0&loginFailureCount=0&sIdString=aa95f380-e08f-40a7-af8a-8ac45872793b&pkSupported=true&parentPageKey=d_checkpoint_lg_consumerLogin&trk=&authUUID=&session_redirect=&loginCsrfParam=0fdb8488-af79-4116-8c70-a6a8927a9565&fp_data=default&_d=d&showGoogleOneTapLogin=true&showAppleLogin=true&showMicrosoftLogin=true&controlId=d_checkpoint_lg_consumerLogin-login_submit_button&session_password=Ghosh%4039039820"
headers = {
  'Host': 'www.linkedin.com',
  'Content-Length': '488',
  'Cache-Control': 'max-age=0',
  'Sec-Ch-Ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
  'Sec-Ch-Ua-Mobile': '?0',
  'Sec-Ch-Ua-Platform': '"Linux"',
  'Accept-Language': 'en-GB,en;q=0.9',
  'Upgrade-Insecure-Requests': '1',
  'Origin': 'https://www.linkedin.com',
  'Content-Type': 'application/x-www-form-urlencoded',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-User': '?1',
  'Sec-Fetch-Dest': 'document',
  'Referer': 'https://www.linkedin.com/checkpoint/lg/sign-in-another-account',
  'Accept-Encoding': 'gzip, deflate, br',
  'Priority': 'u=0, i',
  'Cookie': 'bcookie="v=2&0fdb8488-af79-4116-8c70-a6a8927a9565"; bscookie="v=1&202409161445530a99f3d7-60cd-4031-8086-7f6911a8ac5eAQGr3Eg2sncDPuzEoEzY6yZ3p1D868pX"; JSESSIONID=ajax:1604855610149830055; bcookie="v=2&0fdb8488-af79-4116-8c70-a6a8927a9565"; lang=v=2&lang=en-us;'
}

response = session.post(url, headers=headers, data=payload)
print(session.cookies)
