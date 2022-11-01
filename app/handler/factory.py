from datetime import datetime


class ResponseFactory(object):

    @staticmethod
    def model_to_dict(objs, *ignore: str):
        data_list = []

        #区分objs是单个对象还是列表,1代表对象，0代表列表
        flag = 0
        if not isinstance(objs,list):
            flag = 1
            objs = [objs]
        for obj in objs:
            data = dict()
            for c in obj.__table__.columns:
                if c.name in ignore:
                    # 如果字段忽略, 则不进行转换
                    continue
                val = getattr(obj, c.name)
                if isinstance(val, datetime):
                    data[c.name] = val.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    data[c.name] = val
            data_list.append(data)
        if flag:
            return data_list[0]
        return data_list

    @staticmethod
    def model_to_list(data: list, *ignore: str):
        return [ResponseFactory.model_to_dict(x, *ignore) for x in data]
