from setuptools import setup, find_packages

setup(
    name='ocacaptcha',
    version='0.2.3',
    packages=find_packages(),
    author='Nazarii',
    install_requires=[
        'requests',
        'selenium',
        # Другие зависимости вашего пакета
    ],
    entry_points={
        'console_scripts': [
            'oca_solve_captcha = ocacaptcha.captcha_solver:oca_solve_captcha',
            # Замените module_name и oca_solve_captcha_func на ваши реальные имена
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
