# import streamlit as st

# st.set_page_config(
#     page_title="Wattter.估值计算",
#     page_icon="🍄",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     )

# def calculate_dcf(net_profit, depreciation, capital_expenditure, working_capital_change, growth_rate, discount_rate, long_term_growth_rate, years, total_shares, terminal_year):
#     """
#     计算DCF估值模型。
    
#     参数:
#     net_profit (float): 净利润
#     depreciation (float): 折旧与摊销
#     capital_expenditure (float): 资本支出
#     working_capital_change (float): 营运资本变动
#     growth_rate (float): 自由现金流增长率
#     discount_rate (float): 折现率
#     long_term_growth_rate (float): 长期增长率
#     years (int): 预测年数
#     total_shares (float): 总股票数量
#     terminal_year (int): 终值计算年份

#     返回:
#     total_company_value (float): 公司总价值
#     intrinsic_value_per_share (float): 每股内在价值
#     """
#     # 计算初始自由现金流
#     initial_fcf = net_profit + depreciation - capital_expenditure - working_capital_change
#     fcf_values = []

#     # 计算每年的自由现金流及其现值
#     for i in range(1, years + 1):
#         fcf = initial_fcf * ((1 + growth_rate) ** i)
#         pv_fcf = fcf / ((1 + discount_rate) ** i)
#         fcf_values.append(pv_fcf)

#     # 使用最后一年的自由现金流来计算终值
#     final_fcf = fcf_values[-1]  # 使用最后一年的自由现金流
#     terminal_value = final_fcf * (1 + long_term_growth_rate) / (discount_rate - long_term_growth_rate)
#     pv_terminal_value = terminal_value / ((1 + discount_rate) ** terminal_year)

#     # 计算公司总价值和每股内在价值
#     total_company_value = sum(fcf_values) + pv_terminal_value
#     intrinsic_value_per_share = total_company_value / total_shares

#     return total_company_value, intrinsic_value_per_share

# def val_formula_1(net_profit, risk_free_rate, discount_rate, total_shares):
#     """
#     通过无风险收益率和折扣率计算公司估值。

#     参数:
#     net_profit (float): 净利润
#     risk_free_rate (float): 无风险收益率
#     discount_rate (float): 折扣率

#     返回:
#     company_valuation (float): 公司估值
#     """
#     annual_yield = net_profit / risk_free_rate
#     company_valuation = annual_yield * discount_rate
#     valuation_per_share = company_valuation / total_shares
#     return company_valuation, valuation_per_share

# def val_formula_2(net_profit, market_value, cash, risk_free_rate):
#     """
#     计算扣除现金后的资产收益率。

#     参数:
#     net_profit (float): 净利润
#     market_value (float): 市值
#     cash (float): 现金
#     risk_free_rate (float): 无风险收益率

#     返回:
#     earning_yield (float): 扣现金资产收益率
#     """
#     earning_yield = net_profit / (market_value - cash)
#     return earning_yield

# # Streamlit 页面布局
# # 初始值定义，将变量放在全局，确保在侧边栏和主页面都可以访问
# if 'total_company_value' not in st.session_state:
#     st.session_state.total_company_value = 0
#     st.session_state.intrinsic_value_per_share = 0
#     st.session_state.company_valuation = 0
#     st.session_state.earning_yield = 0

# # 确保所有变量已被初始化
# st.session_state.setdefault('total_company_value', 0)
# st.session_state.setdefault('intrinsic_value_per_share', 0)
# st.session_state.setdefault('company_valuation', 0)
# st.session_state.setdefault('valuation_per_share', 0)
# st.session_state.setdefault('earning_yield', 0)

# with st.sidebar:
#     st.header('输入参数')
#     st.write('财务参数：')
#     market_value = st.number_input('市值（亿元）', value=100.0)
#     total_shares = st.number_input('总股票数量（亿股）', value=12.5)
#     current_price_per_share = st.number_input('每股当前价格（元）', value=8.0)
#     net_profit = st.number_input('净利润（亿元）', value=1.0)
#     cash = st.number_input('现金（亿元）', value=10.0)
#     depreciation = st.number_input('折旧与摊销（亿元）', value=0.1)
#     capital_expenditure = st.number_input('资本支出（亿元）', value=0.2)
#     working_capital_change = st.number_input('营运资本变动（亿元）', value=0.1)
#     st.divider()
#     st.write('主观比率参数：')
#     growth_rate = st.number_input('自由现金流增长率（%）', value=5.0)
#     discount_rate_dcf = st.number_input('DCF折现率/无风险利率（%）', value=6.0)
#     long_term_growth_rate = st.number_input('预期长期增长率（%）', value=3.0)
#     years = st.number_input('预测期（年）', value=10, step=1)
#     risk_free_rate = st.number_input('无风险收益率（%）', value=5.0)
#     discount_rate_val1 = st.number_input('估值折扣率（%）', value=60.0)
#     calculate_button = st.button('计算估值')

# if calculate_button:
#     st.session_state.total_company_value, st.session_state.intrinsic_value_per_share = calculate_dcf(
#         net_profit * 1e9,
#         depreciation * 1e9,
#         capital_expenditure * 1e9,
#         working_capital_change * 1e9,
#         growth_rate / 100,
#         discount_rate_dcf / 100,
#         long_term_growth_rate / 100,
#         years,
#         total_shares * 1e9,
#         years
#     )
    
#     st.session_state.company_valuation, st.session_state.valuation_per_share = val_formula_1(
#         net_profit * 1e9, 
#         risk_free_rate / 100, 
#         discount_rate_val1 / 100,
#         total_shares * 1e9
#     )
    
#     st.session_state.earning_yield = val_formula_2(
#         net_profit * 1e9, 
#         market_value * 1e9, 
#         cash * 1e9, 
#         risk_free_rate / 100
#     )

#     # 强制刷新页面以显示结果
#     st.experimental_rerun()

# # 显示估值结果对比
# if 'total_company_value' in st.session_state:
#     st.header('估值结果对比')
#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         st.write('当前市值（亿元）')
#         st.write(f'{market_value:.2f}')
#         st.write('每股当前价格（元）')
#         st.write(f'{current_price_per_share:.2f}')
#     with col2:
#         st.write('DCF估值（亿元）')
#         st.write(f'{st.session_state.total_company_value / 1e9:.2f}')
#         st.write('DCF每股估值（元）')
#         st.write(f'{st.session_state.intrinsic_value_per_share:.2f}')
#     with col3:
#         st.write('无风险收益对比估值（亿元）')
#         st.write(f'{st.session_state.company_valuation / 1e9:.2f}')
#         st.write('无风险每股估值（元）')
#         st.write(f'{st.session_state.valuation_per_share:.2f}')
#     with col4:
#         st.write('企业扣现金资产收益率')
#         st.write(f'{st.session_state.earning_yield:.2%}')
#         st.write('无风险收益率')
#         st.write(f'{risk_free_rate:.2f}%')

#     # 显示估值分析
#     st.write('### 估值分析')
#     if market_value < st.session_state.total_company_value / 1e9:
#         st.write('根据DCF模型，股票可能被 低估🔥。')
#     else:
#         st.write('根据DCF模型，股票可能被 高估🧊。')

#     if market_value < st.session_state.company_valuation / 1e9:
#         st.write('根据无风险收益对比估值，股票可能被 低估🔥。')
#     else:
#         st.write('根据无风险收益对比估值，股票可能被 高估🧊。')

#     if st.session_state.earning_yield > (risk_free_rate / 100):
#         st.write('根据企业扣现金资产收益率，此收益率超过无风险收益率，长期可持续的话，可考虑投资🔥。')
#     else:
#         st.write('根据企业扣现金资产收益率，此收益率未超过无风险收益率，需谨慎考虑🧊。')


import streamlit as st

# 配置页面的基本属性
st.set_page_config(
    page_title="Wattter.估值计算",
    page_icon="🍄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 定义DCF估值计算函数
def calculate_dcf(net_profit, depreciation, capital_expenditure, working_capital_change, growth_rate, discount_rate, long_term_growth_rate, years, total_shares, terminal_year):
    """
    计算DCF估值模型。
    
    参数:
    net_profit (float): 净利润
    depreciation (float): 折旧与摊销
    capital_expenditure (float): 资本支出
    working_capital_change (float): 营运资本变动
    growth_rate (float): 自由现金流增长率
    discount_rate (float): 折现率
    long_term_growth_rate (float): 长期增长率
    years (int): 预测年数
    total_shares (float): 总股票数量
    terminal_year (int): 终值计算年份

    返回:
    total_company_value (float): 公司总价值
    intrinsic_value_per_share (float): 每股内在价值
    """
    initial_fcf = net_profit + depreciation - capital_expenditure - working_capital_change
    fcf_values = []
    for i in range(1, years + 1):
        fcf = initial_fcf * ((1 + growth_rate) ** i)
        pv_fcf = fcf / ((1 + discount_rate) ** i)
        fcf_values.append(pv_fcf)
    final_fcf = fcf_values[-1]
    terminal_value = final_fcf * (1 + long_term_growth_rate) / (discount_rate - long_term_growth_rate)
    pv_terminal_value = terminal_value / ((1 + discount_rate) ** terminal_year)
    total_company_value = sum(fcf_values) + pv_terminal_value
    intrinsic_value_per_share = total_company_value / total_shares
    return total_company_value, intrinsic_value_per_share

# 定义无风险收益对比估值函数
def val_formula_1(net_profit, risk_free_rate, discount_rate, total_shares):
    """
    通过无风险收益率和折扣率计算公司估值。
    
    参数:
    net_profit (float): 净利润
    risk_free_rate (float): 无风险收益率
    discount_rate (float): 折扣率
    total_shares (float): 总股票数量

    返回:
    company_valuation (float): 公司估值
    valuation_per_share (float): 每股估值
    """
    annual_yield = net_profit / risk_free_rate
    company_valuation = annual_yield * discount_rate
    valuation_per_share = company_valuation / total_shares
    return company_valuation, valuation_per_share

# 定义资产收益率计算函数
def val_formula_2(net_profit, market_value, cash, risk_free_rate):
    """
    计算扣除现金后的资产收益率。
    
    参数:
    net_profit (float): 净利润
    market_value (float): 市值
    cash (float): 现金
    risk_free_rate (float): 无风险收益率

    返回:
    earning_yield (float): 扣现金资产收益率
    """
    earning_yield = net_profit / (market_value - cash)
    return earning_yield

# 初始化session_state中的变量
for key in ['total_company_value', 'intrinsic_value_per_share', 'company_valuation', 'valuation_per_share', 'earning_yield']:
    st.session_state.setdefault(key, 0)

# 用户输入参数界面布局
with st.sidebar:
    st.header('输入参数')
    st.subheader('财务参数：')
    market_value = st.number_input('市值（亿元）', value=100.0)
    total_shares = st.number_input('总股票数量（亿股）', value=12.5)
    current_price_per_share = st.number_input('每股当前价格（元）', value=8.0)
    net_profit = st.number_input('净利润（亿元）', value=1.0)
    cash = st.number_input('现金（亿元）', value=10.0)
    depreciation = st.number_input('折旧与摊销（亿元）', value=0.1)
    capital_expenditure = st.number_input('资本支出（亿元）', value=0.2)
    working_capital_change = st.number_input('营运资本变动（亿元）', value=0.1)
    st.subheader('主观比率参数：')
    growth_rate = st.number_input('自由现金流增长率（%）', value=5.0)
    discount_rate_dcf = st.number_input('DCF折现率/无风险利率（%）', value=6.0)
    long_term_growth_rate = st.number_input('预期长期增长率（%）', value=3.0)
    years = st.number_input('预测期（年）', value=10, step=1)
    risk_free_rate = st.number_input('无风险收益率（%）', value=5.0)
    discount_rate_val1 = st.number_input('估值折扣率（%）', value=60.0)
    calculate_button = st.button('计算估值')

# 计算估值并显示结果
if calculate_button:
    st.session_state.total_company_value, st.session_state.intrinsic_value_per_share = calculate_dcf(
        net_profit * 1e9,
        depreciation * 1e9,
        capital_expenditure * 1e9,
        working_capital_change * 1e9,
        growth_rate / 100,
        discount_rate_dcf / 100,
        long_term_growth_rate / 100,
        years,
        total_shares * 1e9,
        years
    )
    st.session_state.company_valuation, st.session_state.valuation_per_share = val_formula_1(
        net_profit * 1e9, 
        risk_free_rate / 100, 
        discount_rate_val1 / 100,
        total_shares * 1e9
    )
    st.session_state.earning_yield = val_formula_2(
        net_profit * 1e9, 
        market_value * 1e9, 
        cash * 1e9, 
        risk_free_rate / 100
    )
st.header('估值结果对比')
# 显示估值结果和分析
if calculate_button:
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write('当前市值（亿元）')
        st.write(f'{market_value:.2f}')
        st.write('每股当前价格（元）')
        st.write(f'{current_price_per_share:.2f}')
    with col2:
        st.write('DCF估值（亿元）')
        st.write(f'{st.session_state.total_company_value / 1e9:.2f}')
        st.write('DCF每股估值（元）')
        st.write(f'{st.session_state.intrinsic_value_per_share:.2f}')
    with col3:
        st.write('无风险收益对比估值（亿元）')
        st.write(f'{st.session_state.company_valuation / 1e9:.2f}')
        st.write('无风险每股估值（元）')
        st.write(f'{st.session_state.valuation_per_share:.2f}')
    with col4:
        st.write('企业扣现金资产收益率')
        st.write(f'{st.session_state.earning_yield:.2%}')
        st.write('无风险收益率')
        st.write(f'{risk_free_rate:.2f}%')

    # 显示估值分析
    st.write('### 估值分析')
    if market_value < st.session_state.total_company_value / 1e9:
        st.write('根据DCF模型，股票可能被低估🔥。')
    else:
        st.write('根据DCF模型，股票可能被高估🧊。')

    if market_value < st.session_state.company_valuation / 1e9:
        st.write('根据无风险收益对比估值，股票可能被低估🔥。')
    else:
        st.write('根据无风险收益对比估值，股票可能被高估🧊。')

    if st.session_state.earning_yield > (risk_free_rate / 100):
        st.write('根据企业扣现金资产收益率，此收益率超过无风险收益率，长期可持续的话，可考虑投资🔥。')
    else:
        st.write('根据企业扣现金资产收益率，此收益率未超过无风险收益率，需谨慎考虑🧊。')





