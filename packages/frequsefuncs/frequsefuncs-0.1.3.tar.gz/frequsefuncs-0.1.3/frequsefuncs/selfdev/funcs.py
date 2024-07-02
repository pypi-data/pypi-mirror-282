






#输入df和希望呈现的数字格式（'{:,}'、'{:.2%}'、'{:,.0f}'），呈现带格式的表格
def func_format_display(df, num_fmt):
    all_props = [
        ('border','2px solid black'),
    ]
    th_props = [
        ('font-size', '11px'),
        ('text-align', 'center'),
        ('font-weight', 'bold'),
        ('color', 'black'),               ## #6d6d6d
        ('background-color', 'white'),    ## #f7f7f9
        ('border','1px dashed black')
    ]
    td_props = [
        ('font-size', '9px'),
        ('text-align', 'right'),
        ('color', 'black'),
        ('background-color', 'white'),    ## #f7f7f9
        ('border','1px dashed black')
    ]

    config_fmt = [{'selector':'','props':all_props}, 
                  {'selector':'th','props':th_props},
                  {'selector':'td','props':td_props}
                 ]
    dict_fmt = {}
    lst_barfmt = []
    for k in df.columns:
        dict_fmt[k] = num_fmt   #'{:,}' #'{:.2%}' #'{:,.0f}'
        lst_barfmt.append(k)
    display(df.style.set_table_styles(config_fmt).format(dict_fmt).bar(subset = lst_barfmt, width = 80, align = 'mid'))




#输入df和希望呈现的数字格式（'{:,}'、'{:.2%}'、'{:,.0f}'），呈现带格式的表格
def func_format_display_bycol(df, dict_fmt, lst_barfmt):
    all_props = [
        ('border','2px solid black'),
    ]
    th_props = [
        ('font-size', '11px'),
        ('text-align', 'center'),
        ('font-weight', 'bold'),
        ('color', 'black'),               ## #6d6d6d
        ('background-color', 'white'),    ## #f7f7f9
        ('border','1px dashed black')
    ]
    td_props = [
        ('font-size', '9px'),
        ('text-align', 'right'),
        ('color', 'black'),
        ('background-color', 'white'),    ## #f7f7f9
        ('border','1px dashed black')
    ]

    config_fmt = [{'selector':'','props':all_props}, 
                  {'selector':'th','props':th_props},
                  {'selector':'td','props':td_props}
                 ]
    display(df.style.set_table_styles(config_fmt).format(dict_fmt).bar(subset = lst_barfmt, width = 80, align = 'mid'))







def func_parse_var_n_val(str_sql, str_var_head):
    '''
    输入一段字符串
    解析出变量名称和sql字符串，并赋值（全局变量）
    返回变量名
    '''
    s = str_sql.strip()                                #去掉字符串前后的空格等
    ptn = '@({}.*?):\n((?s:.)*)'.format(str_var_head)  #匹配变量名和将要赋的值。(?s:.) matches any character regardless of flags
    str_var_nm, str_var_val = re.findall(ptn, s)[0]    #匹配变量名和将要赋的值
    globals()[str_var_nm] = str_var_val                #赋值，用globals()建全局变量
    return str_var_nm


def func_read_sql_from_file(fpath_str_sql, str_split, str_var_head):
    '''
    读入制定文件内的sql字符串，并按标注分别给每段sql赋值到全局变量
    '''
    with open(fpath_str_sql, 'r') as f:
        str_sqls = f.read()
    
    #解析读入的sql字符串，分段进行赋值（全局变量）
    lst_str_sql = str_sqls.split(str_split)   #将各段sql以字符串形式存入列表
    lst_str_sql_var = []                      #准备存放各段sql的变量名
    for str_sql in lst_str_sql:
        try:
            str_sql_var  = func_parse_var_n_val(str_sql, str_var_head)
            lst_str_sql_var.append(str_sql_var)
        except:
            print(str_sql)
            raise
    return lst_str_sql_var











