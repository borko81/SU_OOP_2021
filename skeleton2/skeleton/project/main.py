# from system import System


# def zero_test():
#     System.register_power_hardware("HDD", 200, 200)
#     System.register_heavy_hardware("SSD", 400, 400)
#     print(System.analyze())
#
#     # for i in System._hardware:
#     #     print(i.memory)
#
#     System.register_light_software("HDD", "Test", 0, 10)
#     print(System.register_express_software("HDD", "Test2", 100, 100))
#     System.register_express_software("HDD", "Test3", 50, 100)
#     System.register_light_software("SSD", "Windows", 20, 50)
#     System.register_express_software("SSD", "Linux", 50, 100)
#     System.register_light_software("SSD", "Unix", 20, 50)
#     print(System.analyze())
#     System.release_software_component("SSD", "Linux")
#     print(System.system_split())
#     #print([n.memory for n in System._hardware if n.name == 'HDD'])


# 455
if __name__ == "__main__":
    def br():
        raise Exception('Error')

    try:
        a = br()
        print(a)
    except Exception as e:
        print(e)
