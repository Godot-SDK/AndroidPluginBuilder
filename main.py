import os 
from shutil import copyfile

def create_project():
    plugin_name = input("请输出你要创建的插件名称\n")
    create_dirs = ["godot-lib", "gradle", "gradle/wrapper", "docs", plugin_name, plugin_name + "/src", plugin_name + "/src/main",  plugin_name + "/src/main/java",  plugin_name + "/src/main/res"]
    for dir in create_dirs:
        os.mkdir(dir)

    with open(".gitignore", "w", encoding="utf-8") as gitignore:
        gitignore.write("")

    with open("gradle.properties", "w+", encoding="utf-8") as gradle_properties:
        gradle_properties.write("android.useAndroidX=true\n")
        gradle_properties.write("enableJetifier=true")
    
    with open("settings.gradle", "w+", encoding="utf-8") as settings:
        settings.write("include " + "'" + ":" + "godot-lib\n")
        settings.write("include " + "'" + ":" + plugin_name)

    # build resource
    copyfile("resource/gradlew", "gradlew")
    copyfile("resource/gradlew.bat", "gradlew.bat")

    pass

def remove_project():

    pass

print("创建完成工程，请自行补充java代码细节和目录包名！")
main_action = input("请输入你要的操作，y：创建安卓工程，n:删除工程")

if main_action == "y":
    create_project()

if main_action == "n":
    remove_project()


