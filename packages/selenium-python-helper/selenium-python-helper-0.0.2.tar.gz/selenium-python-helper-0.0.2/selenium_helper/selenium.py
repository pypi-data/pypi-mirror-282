# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  selenium-python-helper
# FileName:     selenium.py
# Description:  TODO
# Author:       mfkifhss2023
# CreateDate:   2024/06/28
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import os
import string
import zipfile
import selenium
from abc import abstractmethod
from seleniumwire import webdriver as driver_wire
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium_helper.libs import logger
from selenium_helper.http import get_proxy_address
from selenium_helper.dir import get_project_path, get_chrome_default_user_data_path, get_var_path, is_file, \
    get_browser_bin_exe, create_directory, move_file, is_dir, get_browser_process_name, is_process_running, \
    join_path


class Browser(object):
    TIMEOUT = 10
    LOG_LEVEL = "DEBUG"
    BROWSER_NAME = None
    LOG_PATH = os.path.join(get_project_path(), "log")
    create_directory(LOG_PATH)
    BIN_PATH = os.path.join(get_project_path(), "bin")
    create_directory(BIN_PATH)
    USERDATA_PATH = None
    IMAGE_PATH = os.path.join(get_project_path(), "image")
    create_directory(IMAGE_PATH)

    def __init__(self, browser_path: str, is_headless: bool = True, proxy_address: str = '', proxy_username: str = '',
                 proxy_password: str = '', proxy_scheme: str = "http", is_enable_proxy: bool = False,
                 enable_cdp: bool = False) -> None:
        self.browser_path = browser_path
        self.is_headless = is_headless
        self.proxy_address = proxy_address
        self.is_enable_proxy = is_enable_proxy
        self.proxy_scheme = proxy_scheme
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password
        self.enable_cdp = enable_cdp

    @abstractmethod
    def get_browser(self):
        pass

    @classmethod
    def get_options(cls):
        pass

    @abstractmethod
    def get_service(self):
        pass

    @abstractmethod
    def is_running(self):
        pass


class ChromeBrowser(Browser):
    BROWSER_NAME = "Chrome"

    def __init__(self, browser_path: str, is_headless: bool = True, proxy_address: str = "", proxy_username: str = "",
                 proxy_password: str = "", proxy_scheme: str = "http", is_enable_proxy: bool = False,
                 enable_cdp: bool = False) -> None:
        super().__init__(browser_path, is_headless, proxy_address, proxy_username, proxy_password, proxy_scheme,
                         is_enable_proxy, enable_cdp)
        self.driver_file = os.path.join(self.BIN_PATH, "chromedriver.exe")
        if is_file(self.driver_file) is False:
            logger.warning("开始下载与浏览器版本匹配的chromedriver.exe文件.")
            # 自动下载并安装适用于当前 Chrome 版本的 chromedriver
            driver_path = ChromeDriverManager().install()
            move_file(src_file=driver_path, dst_path=self.BIN_PATH)
            logger.warning("chromedriver.exe文件下载完成.")
        self.__bind_chrome_user_data_dir()

    def __bind_chrome_user_data_dir(self) -> None:
        self.USERDATA_PATH = get_chrome_default_user_data_path()
        if is_dir(self.USERDATA_PATH) is False:
            self.USERDATA_PATH = os.path.sep.join([os.getcwd(), "profile", "chrome-profile"])
            create_directory(self.USERDATA_PATH)
        logger.warning("浏览器用户的数据目录为: {}".format(self.USERDATA_PATH))

    def get_options(self) -> Options:
        # 支持的浏览器有: Firefox, Chrome, Ie, Edge, Opera, Safari, BlackBerry, Android, PhantomJS等
        chrome_options = driver_wire.ChromeOptions()
        # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--disable-gpu')
        # 隐身模式（无痕模式）
        # chrome_options.add_argument('--incognito')
        # 隐藏"Chrome正在受到自动软件的控制"
        chrome_options.add_argument('disable-infobars')
        # 禁用 WebRTC
        chrome_options.add_argument("--disable-webrtc")
        chrome_options.add_argument('--user-data-dir={}'.format(self.USERDATA_PATH))
        # chrome_options.add_argument("--disable-autofill-passwords")  # 禁用自动填充密码
        # chrome_options.add_argument("--disable-save-password-bubble")  # 禁用保存密码提示框
        # 在 ChromeOptions 中禁用缓存
        # chrome_options.add_argument("--disable-cache")
        # chrome_options.add_argument("--disk-cache-size=0")
        # 设置中文
        # chrome_options.add_argument('lang=zh_CN.UTF-8')
        # chrome_options.add_argument('--no-sandbox')  # linux下
        if self.is_headless is True:
            # 谷歌浏览器后台运行模式
            chrome_options.add_argument('--headless')
            # 指定浏览器分辨率
            # chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument('--window-size=2560,1440')
        else:
            # 浏览器最大化
            chrome_options.add_argument('--start-maximized')
        if self.enable_cdp is True:
            chrome_options.add_argument('--auto-open-devtools-for-tabs')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # 或者使用下面的设置, 提升速度
        # chrome_options.add_argument('blink-settings=imagesEnabled=false')
        # 隐藏滚动条, 应对一些特殊页面
        # chrome_options.add_argument('--hide-scrollbars')
        # chrome_options.add_argument('--remote-debugging-port=9222')
        chrome_options.add_argument('--log-level=3')
        # 手动指定使用的浏览器位置，如果谷歌浏览器的安装目录配置在系统的path环境变量中，那么此处可以不传路径
        logger.warning("当前系统Chrome浏览器可运行程序的路径为：{}".format(self.browser_path))
        chrome_options.binary_location = self.browser_path
        # 添加代理设置到 Chrome 选项
        if self.is_enable_proxy is True:
            if not self.proxy_address:
                ip_addr = get_proxy_address()
                if ip_addr:
                    self.proxy_address = ip_addr
            if self.proxy_address:
                chrome_options.add_argument('--proxy-server=http://{}'.format(self.proxy_address))
                chrome_options.add_argument('--proxy-server=https://{}'.format(self.proxy_address))
                # proxy_plugin_path = self.__create_proxy_extension()
                # proxy_plugin_path = proxy_plugin_path if isinstance(proxy_plugin_path, str)
                # else str(proxy_plugin_path)
                # chrome_options.add_extension(proxy_plugin_path)
                # logger.warning("{}代理插件添加完成".format(self.BROWSER_NAME))
        logger.warning("使用代理地址：{}".format(self.proxy_address or "null"))
        pre = dict()
        # 设置这两个参数就可以避免密码提示框的弹出
        pre["credentials_enable_service"] = False
        pre["profile.password_manager_enabled"] = False
        # pre["profile.default_content_settings.popups"] = 0
        # 禁止加载图片
        # pre["profile.managed_default_content_settings.images"] = 2
        chrome_options.add_experimental_option("prefs", pre)
        chrome_options.add_experimental_option('useAutomationExtension', False)
        # 关闭devtools工具,
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        return chrome_options

    def get_service(self) -> ChromeService:
        # 指定chrome_driver路径
        # chrome_driver = r"C:\Python\spiderStudyProject\driver\chromedriver.exe"
        # 指定chrome_driver记录的日志信息
        log_file = os.path.join(self.LOG_PATH, "chrome.log")
        # 如果selenium的版本高于4.6，则不需要配置executable_path参数
        # 指定chrome_driver记录的日志信息
        logger.warning("ChromedDriver路径：{}".format(self.driver_file))
        service = ChromeService(
            executable_path=self.driver_file,
            service_args=['--log-level={}'.format(self.LOG_LEVEL), '--append-log', '--readable-timestamp'],
            log_output=log_file
        )
        return service

    def get_browser(self) -> tuple:
        service = self.get_service()
        options = self.get_options()
        browser = driver_wire.Chrome(service=service, options=options)
        logger.warning("Selenium 版本: {}".format(selenium.__version__))
        logger.warning("浏览器版本: {}".format(browser.capabilities['browserVersion']))
        # 设置隐式等待时间为3秒
        # browser.implicitly_wait(3)
        # 反屏蔽
        browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})',
        })
        if self.enable_cdp is True:
            # 启用 DevTools 并启用网络日志
            browser.execute_cdp_cmd('Network.enable', {})
        wait = WebDriverWait(driver=browser, timeout=self.TIMEOUT)
        return browser, wait, self.BROWSER_NAME

    def is_running(self) -> bool:
        process_name = get_browser_process_name(self.BROWSER_NAME)
        return is_process_running(process_name=process_name)

    def __create_proxy_extension(self):
        """Proxy Auth Extension
        args:
            proxy_host (str): domain or ip address, ie proxy.domain.com
            proxy_port (int): port
            proxy_username (str): auth username
            proxy_password (str): auth password
        kwargs:
            scheme (str): proxy scheme, default http
            plugin_path (str): absolute path of the extension
        return str -> plugin_path
        """
        proxy_address_slice = self.proxy_address.split(":")
        plugin_path = join_path([get_project_path(), 'bin', 'Selenium-Chrome-HTTP-Private-Proxy.zip'])
        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """
        background_js = string.Template(
            """
            var config = {
                    mode: "fixed_servers",
                    rules: {
                      singleProxy: {
                        scheme: "${scheme}",
                        host: "${host}",
                        port: parseInt(${port})
                      },
                      bypassList: ["foobar.com"]
                    }
                  };
            chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
            function callbackFn(details) {
                return {
                    authCredentials: {
                        username: "${username}",
                        password: "${password}"
                    }
                };
            }
            chrome.webRequest.onAuthRequired.addListener(
                        callbackFn,
                        {urls: ["<all_urls>"]},
                        ['blocking']
            );
            """
        ).substitute(
            host=proxy_address_slice[0],
            port=proxy_address_slice[1],
            username=self.proxy_username,
            password=self.proxy_password,
            scheme=self.proxy_scheme,
        )
        with zipfile.ZipFile(plugin_path if isinstance(plugin_path, str) else str(plugin_path), 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)

        return plugin_path


class FirefoxBrowser(Browser):
    BROWSER_NAME = "Firefox"

    def __init__(self, browser_path: str, is_headless: bool = True, proxy_address: str = "", proxy_username: str = "",
                 proxy_password: str = "", proxy_scheme: str = "http", is_enable_proxy: bool = False,
                 enable_cdp: bool = False) -> None:
        super().__init__(browser_path, is_headless, proxy_address, proxy_username, proxy_password, proxy_scheme,
                         is_enable_proxy, enable_cdp)

    def get_options(self) -> FirefoxOptions:
        firefox_profile = FirefoxOptions()
        # 在无头模式下运行 Firefox
        firefox_profile.headless = self.is_headless
        # 设置代理
        # options.add_argument('--proxy-server=http://proxy.example.com:8080')
        logger.warning("获取的浏览器可运行文件路径为：{}".format(self.browser_path))
        firefox_profile.binary_location = self.browser_path
        # 禁止浏览器自动填充账号，密码
        firefox_profile.set_preference('signon.autofillForms', False)  # 禁止自动填充表单
        firefox_profile.set_preference('signon.autologin.proxy', False)
        firefox_profile.set_preference("signon.rememberSignons", False)  # 不保存密码
        firefox_profile.set_preference('signon.storeWhenAutocompleteOff', False)
        return firefox_profile

    @classmethod
    def get_service(cls) -> FirefoxService:
        # geckodriver 驱动路径
        # gecko_driver_path = '/path/to/geckodriver'
        # 指定gecko_driver记录的日志信息
        log_file = os.path.join(cls.LOG_PATH, "firefox.log")
        # 如果selenium的版本高于4.6，则不需要配置executable_path参数
        service = FirefoxService(
            # executable_path=gecko_driver_path,
            service_args=['--log={}'.format(cls.LOG_LEVEL.lower())],
            log_output=log_file
        )
        return service

    def get_browser(self) -> tuple:
        options = self.get_options()
        service = self.get_service()
        browser = Firefox(service=service, options=options)
        # 设置隐式等待时间为3秒
        # browser.implicitly_wait(3)
        wait = WebDriverWait(driver=browser, timeout=self.TIMEOUT)
        return browser, wait, self.BROWSER_NAME

    def is_running(self) -> bool:
        process_name = get_browser_process_name(self.BROWSER_NAME)
        return is_process_running(process_name=process_name)


class SeleniumProxy(object):

    def __init__(self, browser_name: str, proxy_address: str = "", proxy_username: str = "", enable_cdp: bool = False,
                 proxy_scheme: str = "http", proxy_password: str = "", is_enable_proxy: bool = False,
                 browser_path: str = None, is_headless: bool = True, is_single_instance: bool = True) -> None:
        if browser_path:
            if not is_file(browser_path):
                raise ValueError("browser path is not exist")
        else:
            browser_path = get_var_path(var=browser_name)
            if not browser_path:
                raise ValueError("system not installed {} browser.".format(browser_name))
        exe_name = get_browser_bin_exe(browser_name=browser_name)
        exe_file = os.path.join(browser_path, exe_name)
        if browser_name == "Chrome":
            self.browser_proxy = ChromeBrowser(
                browser_path=exe_file, is_headless=is_headless, proxy_address=proxy_address, proxy_scheme=proxy_scheme,
                is_enable_proxy=is_enable_proxy, proxy_username=proxy_username, proxy_password=proxy_password,
                enable_cdp=enable_cdp
            )
            # 单实例模式下，系统只能有一个chrome浏览器进程在运行中
            if is_single_instance is True:
                if self.browser_proxy.is_running() is True:
                    raise ValueError("Chrome browser is already running.")
            self.browser, self.wait, self.browser_name = self.browser_proxy.get_browser()
        elif browser_name == "Firefox":
            self.browser_proxy = FirefoxBrowser(
                browser_path=exe_file, is_headless=is_headless, proxy_address=proxy_address, proxy_scheme=proxy_scheme,
                proxy_password=proxy_password, is_enable_proxy=is_enable_proxy, proxy_username=proxy_username,
                enable_cdp=enable_cdp
            )
            # 单实例模式下，系统只能有一个firefox浏览器进程在运行中
            if is_single_instance is True:
                if self.browser_proxy.is_running() is True:
                    raise ValueError("Firefox browser is already running.")
            self.browser, self.wait, self.browser_name = self.browser_proxy.get_browser()
        else:
            raise ValueError("Browser name must be Chrome or Firefox.")

    def new_instance(self) -> None:
        self.browser, self.wait, self.browser_name = self.browser_proxy.get_browser()

    def quit(self) -> None:
        self.browser.quit()

    def get(self, url: str) -> None:
        self.browser.get(url)

    def get_current_url(self) -> str:
        return self.browser.current_url

    @classmethod
    def pending(cls) -> None:
        input("请按回车键退出...\n")

    def get_page_source(self) -> str:
        return self.browser.page_source

    def get_session(self) -> str:
        # 使用 JavaScript 获取网络请求的 Cookie 头部信息
        cookies = self.browser.execute_script("return document.cookie")
        return cookies or ''

    def get_cookies(self) -> list:
        return self.browser.get_cookies() or list()

    def get_cookie(self, name: str) -> dict:
        """
        {
        'domain': '.ctrip.com',
         'expiry': 1717525670,
         'httpOnly': True,
         'name': 'cticket',
         'path': '/',
         'sameSite': 'None',
         'secure': True,
         'value': '275F2106E6E6CAAA34E1A32FE2452F42450E99443E2B22A31360D38C0BB2DEB3'
         }
        """
        return self.browser.get_cookie(name=name) or dict()

    def refresh(self) -> None:
        # 刷新当前页面
        self.browser.refresh()
