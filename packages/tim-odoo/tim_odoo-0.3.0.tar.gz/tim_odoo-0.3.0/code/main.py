import hashlib
import hmac


def cal_sign(req, secret):
    queries = dict(req.params)
    keys = [k for k in queries if k not in ["sign", "access_token"]]
    keys.sort()
    input = "".join(k + queries[k] for k in keys)
    input = req.url + input
    input = secret + input + secret
    return generateSHA256(input, secret)


def generateSHA256(input, secret):
    h = hmac.new(secret.encode(), input.encode(), hashlib.sha256)
    return h.hexdigest()
