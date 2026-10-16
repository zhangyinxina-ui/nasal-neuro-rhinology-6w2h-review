#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成《从冷空气30秒流涕到慢性鼻窦炎果冻涕：18篇核心论文十遍精读与张益新双轨鼻炎精准诊疗》
1080P 全高清中文配音科普与学术综述视频 (MP4) 及 5 张高清学术图谱海报 (PNG)。
"""

import os
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

FONT_PATHS = [
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
]

def get_font(size):
    for fp in FONT_PATHS:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except Exception:
                continue
    return ImageFont.load_default()

W, H = 1920, 1080

def create_base_canvas(title, subtitle, badge_text, step_idx, total_steps=5):
    img = Image.new("RGB", (W, H), (11, 18, 33))
    draw = ImageDraw.Draw(img)

    # Top gradient accent bar
    for x in range(W):
        r = int(14 + (56 - 14) * (x / W))
        g = int(165 + (189 - 165) * (x / W))
        b = int(233 + (248 - 233) * (x / W))
        draw.line([(x, 0), (x, 10)], fill=(r, g, b))

    # Header panel
    draw.rounded_rectangle([50, 30, W - 50, 165], radius=18, fill=(19, 30, 52), outline=(45, 75, 120), width=2)

    # Badge
    f_badge = get_font(24)
    draw.rounded_rectangle([75, 48, 390, 92], radius=10, fill=(14, 116, 144))
    draw.text((92, 55), badge_text, font=f_badge, fill=(240, 249, 255))

    # Step indicator
    draw.text((W - 260, 55), f"章节 {step_idx} / {total_steps}", font=f_badge, fill=(125, 211, 252))

    # Title & Subtitle
    f_title = get_font(40)
    f_sub = get_font(24)
    draw.text((415, 46), title, font=f_title, fill=(248, 250, 252))
    draw.text((75, 112), subtitle, font=f_sub, fill=(148, 163, 184))

    # Footer bar
    draw.rounded_rectangle([50, H - 70, W - 50, H - 20], radius=12, fill=(15, 23, 42), outline=(30, 41, 59), width=1)
    f_foot = get_font(20)
    draw.text(
        (75, H - 58),
        "数据来源: arXiv (11篇生物物理/流体力学/AI论文) + Europe PMC (7篇临床鼻科学文献) | GitHub: topsun-bot/nasal-neuro-rhinology-6w2h-review",
        font=f_foot,
        fill=(100, 116, 139),
    )
    return img, draw

def draw_card(draw, box, title, items, accent_color=(56, 189, 248), bg_color=(22, 35, 60)):
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=16, fill=bg_color, outline=accent_color, width=2)
    draw.rounded_rectangle([x1, y1, x2, y1 + 54], radius=16, fill=accent_color)
    draw.rectangle([x1, y1 + 30, x2, y1 + 54], fill=accent_color)
    f_ctitle = get_font(23)
    draw.text((x1 + 18, y1 + 14), title, font=f_ctitle, fill=(11, 18, 33))

    f_item = get_font(20)
    curr_y = y1 + 72
    for line in items:
        if line.startswith("★") or line.startswith("▶") or line.startswith("●"):
            color = (224, 242, 254)
        elif line.startswith("  "):
            color = (148, 163, 184)
        else:
            color = (203, 213, 225)
        draw.text((x1 + 18, curr_y), line, font=f_item, fill=color)
        curr_y += 35

def generate_slide_1():
    img, draw = create_base_canvas(
        "冷空气“30秒流涕”的 6W2H 跨尺度神经-物理反射链",
        "为什么你流的不是发炎脓涕，而是毫秒级 TRPM8 冷觉探头触发的 90,000 个腺体反射性放水？",
        "第一幕 · 6W2H 机制解码",
        1,
    )
    cards = [
        (
            [50, 190, 640, 560],
            "1. What & Why：流的是什么？为什么要流？",
            [
                "● 白色清涕 = 98%水 + 1%盐 + 少量黏蛋白 (MUC5AC)",
                "● 无中性粒细胞/嗜酸细胞，本质是神经反射而非发炎",
                "● 人类鼻腔容积仅 21 mL，较哺乳动物演化缩减 90%",
                "  (Zwicker et al., PNAS 2018, arXiv:1708.08966)",
                "● 特征窄缝水力半径 Rh = 1.5~2.0 mm，前1/3鼻腔",
                "  承担 80% 加温加湿负荷，蒸发冷却峰值 15.6 W/m2",
                "  (Senanayake & Inthavong 2021, arXiv:2107.03641)",
            ],
            (56, 189, 248),
        ),
        (
            [665, 190, 1255, 560],
            "2. Which & When：谁是探头？凭什么30秒？",
            [
                "● 温度探头：三叉神经末梢 TRPM8 (<=26°C, 53 pS)",
                "  与伤害性冷受体 TRPA1 (<17°C, 100 pS)",
                "● 单通道 5闭2开 (5C-2O) 拓扑，双开放态 O1<->O2",
                "  毫秒级簇状钙内流 (Ogloblya 2026, arXiv:2608.23415)",
                "● 蛋白内摩擦激活能倒置 (EcΓ=123 < EoΓ=670 meV)",
                "  在 43.8 meV 极低势垒下实现 Q10≈100 超敏冷激活",
                "● 神经反射=10~30秒 vs 过敏=分钟级 vs 感染=天级",
            ],
            (52, 211, 153),
        ),
        (
            [1280, 190, 1870, 560],
            "3. How & How much：反射弧与 9 万腺体水源",
            [
                "● 传入：鼻前部三叉神经 V1/V2 -> 脑干上泌涎核",
                "● 中转：面神经/翼管神经 -> 翼腭神经节 (PPG) 换元",
                "● 传出：后鼻神经释放 乙酰胆碱(ACh) + VIP",
                "● 水源：90,000 个黏膜下腺 + 200~300 个前部浆液腺",
                "  (Gizurarson 2012, PMC3480721) 瞬间开闸倾泻水盐",
                "● 平时每天分泌 1 升无感咽下；反射爆发时突破",
                "  Rayleigh-Plateau 毛细失稳阈值，十几秒涌出鼻孔！",
            ],
            (251, 191, 36),
        ),
    ]
    for box, t, items, col in cards:
        draw_card(draw, box, t, items, col)

    draw.rounded_rectangle([50, 590, 1870, 985], radius=16, fill=(17, 27, 48), outline=(56, 189, 248), width=2)
    f_flow_title = get_font(27)
    draw.text((75, 610), "完整 30 秒神经反射弧与四级精准拦截靶点图谱（为什么有的治疗有效、有的是智商税）", font=f_flow_title, fill=(125, 211, 252))

    steps = [
        ("① 刺激端", "干冷空气进前鼻阀\n蒸发散热 15.6 W/m2", "【有效拦截】\n保暖口罩 + 33.5°C温盐水\n从源头掐断蒸发冷却", (14, 165, 233)),
        ("② 探头与敏感度端", "三叉神经 TRPM8/TRPA1\n毫秒级 5C-2O 簇状放电", "【有效拦截】\n鼻喷激素 + 鼻喷氮卓斯汀\n调高阈值 V1/2 & 抑神经肽", (16, 185, 129)),
        ("③ 中枢与换元端", "脑干上泌涎核 -> 翼腭神经节\n后鼻神经释放 ACh + VIP", "【终末期拦截】\n后鼻神经冷冻消融 ClariFix\n流涕-1.56分 / 鼻塞-1.51分", (168, 85, 247)),
        ("④ 腺体与血管效应端", "9万腺体M3放水 (ACh)\n海绵窦充血鼻塞 (VIP)", "【精准控水 vs 智商税】\n纯清涕用异丙托溴铵关阀门\n单吃氯雷他定/抗生素=无效", (245, 158, 11)),
    ]
    bx = 75
    for st_title, st_mech, st_rx, col in steps:
        draw.rounded_rectangle([bx, 665, bx + 415, 960], radius=14, fill=(24, 38, 66), outline=col, width=2)
        draw.rounded_rectangle([bx, 665, bx + 415, 712], radius=14, fill=col)
        draw.text((bx + 20, 674), st_title, font=get_font(23), fill=(11, 18, 33))
        draw.text((bx + 20, 728), st_mech, font=get_font(21), fill=(241, 245, 249))
        draw.line([(bx + 20, 805), (bx + 395, 805)], fill=(51, 65, 85), width=2)
        draw.text((bx + 20, 820), st_rx, font=get_font(20), fill=(167, 243, 208))
        if bx < 1300:
            draw.text((bx + 420, 795), "=>", font=get_font(26), fill=(125, 211, 252))
        bx += 450

    out_path = os.path.join(ASSETS_DIR, "slide_01_6w2h.png")
    img.save(out_path)
    return out_path

def generate_slide_2():
    img, draw = create_base_canvas(
        "18篇跨学科核心论文（11篇 arXiv + 7篇 Europe PMC）十遍精读矩阵",
        "横跨 6 个空间数量级 (1 nm 孔道 -> 10 cm 鼻腔) 与 7 个时间数量级 (1 ms 门控 -> 8 h 鼻窦潴留)",
        "第二幕 · 18篇论文十遍精读",
        2,
    )
    clusters = [
        (
            [50, 190, 945, 575],
            "集群 A：鼻腔空气动力学与冷却热通量 (P01, P02, P12)",
            [
                "★ P01 Zwicker 2018 (PNAS / arXiv:1708.08966)",
                "  标量交换效率 E = 1 - exp(-a*L/(Pe*Rh))，人鼻容积 21mL 缩减90%",
                "★ P02 Senanayake & Inthavong 2021 (arXiv:2107.03641)",
                "  前 1/3 鼻腔承担 80% 热湿调节，蒸发潜热主导冷却峰值 15.6 W/m2",
                "★ P12 D'Amato 2018 (Clin Transl Allergy / PMC6031196)",
                "  冷干空气触发胆碱能反射+高渗脱颗粒，异丙托溴铵阻断 >70% 清涕",
            ],
            (56, 189, 248),
        ),
        (
            [975, 190, 1870, 575],
            "集群 B：TRPM8/TRPA1 冷觉受体动力学与统计物理 (P03–P06)",
            [
                "★ P03 Ogloblya & Zholos 2026 (arXiv:2608.23415)",
                "  TRPM8 5闭2开 (5C-2O) 最小拓扑，O1<->O2 直接跃迁驱动毫秒簇状放电",
                "★ P04 Okenov & Moskvin 2021 (JETP Lett / arXiv:2109.05311)",
                "  蛋白内摩擦激活能倒置 (EcΓ=123 < EoΓ=670 meV) 赋予 Q10=100 超敏性",
                "★ P05 Laub & Heimburg 2012 (arXiv:1111.2756) & P06 Maaroufi 2021",
                "  TRPM8 电导 53pS 与脂质膜相变强耦合；外源病毒蛋白直连敏化 TRP",
            ],
            (52, 211, 153),
        ),
        (
            [50, 600, 945, 985],
            "集群 C：气道黏液流变学与薄膜毛细失稳 (P07–P10)",
            [
                "★ P07 Liu & Deng 2025 (arXiv:2510.15562)",
                "  MUC5AC/MUC5B 弹黏塑性水凝胶，二硫键与钙桥交联决定屈服应力 τy",
                "★ P08 Hazra & Picardo 2025a (arXiv:2511.20341)",
                "  黏液膜 Rayleigh-Plateau 对流-绝对失稳相变解释周期性粘液栓形成",
                "★ P09 Hazra 2025b (JFM / arXiv:2502.01883) & P10 Radiom (arXiv:2107.13187)",
                "  黏液脊截留鼻喷药滴；磁线微流变实测 G'≈2.5Pa, η0≈100Pa·s, τR≈20-40s",
            ],
            (251, 191, 36),
        ),
        (
            [975, 600, 1870, 985],
            "集群 D：AI 鼻细胞学、非过敏性鼻病与 PNN 神经消融 (P11, P13–P18)",
            [
                "★ P11 Camporeale & Gelardi 2024 (arXiv:2404.13745)",
                "  深度学习检测 7 类鼻涂片细胞与超微条纹 HSS，秒级区分炎症与神经反射",
                "★ P13 & P14 Kaliner 2009 (PMC3650985 / PMC3650992) & P15 Gizurarson",
                "  确立非过敏性鼻病 (NAR)；90,000 黏膜下腺+200前浆液腺；氮卓斯汀+激素",
                "★ P16 Yoo 2020, P17 Stuyt 2021, P18 Kim 2024 Meta分析 (PMC11566528)",
                "  8项研究472例证实 PNN 冷冻消融12个月流涕降 1.56分、鼻塞降 1.51分",
            ],
            (192, 132, 252),
        ),
    ]
    for box, t, items, col in clusters:
        draw_card(draw, box, t, items, col)

    out_path = os.path.join(ASSETS_DIR, "slide_02_18papers.png")
    img.save(out_path)
    return out_path

def generate_slide_3():
    img, draw = create_base_canvas(
        "核心定量物理模型：TRPM8 内摩擦温度相变 vs 黏液膜毛细失稳",
        "用数学物理方程精确定量：为什么微凉风能打开报警器？为什么猛擤鼻子擤不出果冻涕？",
        "第三幕 · 生物物理定量曲线",
        3,
    )
    draw.rounded_rectangle([50, 190, 935, 985], radius=16, fill=(18, 29, 50), outline=(56, 189, 248), width=2)
    draw.text((80, 210), "模型 1：TRPM8 开放概率 P_open(T) 与病理阈值右移 (P03, P04)", font=get_font(25), fill=(125, 211, 252))
    draw.text((80, 248), "内摩擦激活能 EcΓ=123 meV < Eγ=490 meV < EoΓ=670 meV，能垒 ΔE <= 43.8 meV", font=get_font(19), fill=(148, 163, 184))

    px1, py1, px2, py2 = 140, 310, 880, 740
    draw.rectangle([px1, py1, px2, py2], fill=(12, 20, 36), outline=(71, 85, 105), width=2)
    for i in range(1, 5):
        gy = py1 + i * (py2 - py1) // 5
        draw.line([(px1, gy), (px2, gy)], fill=(30, 41, 59), width=1)
    for idx, temp in enumerate([10, 15, 20, 25, 30, 35, 40]):
        gx = px1 + int((temp - 10) / 30.0 * (px2 - px1))
        draw.line([(gx, py1), (gx, py2)], fill=(30, 41, 59), width=1)
        draw.text((gx - 18, py2 + 12), f"{temp}°C", font=get_font(18), fill=(148, 163, 184))
    draw.text((430, py2 + 45), "鼻黏膜局部表面温度 T (°C)", font=get_font(20), fill=(203, 213, 225))

    sx1 = px1 + int((32 - 10) / 30.0 * (px2 - px1))
    sx2 = px1 + int((35 - 10) / 30.0 * (px2 - px1))
    draw.rectangle([sx1, py1 + 2, sx2, py2 - 2], fill=(6, 78, 59))
    draw.text((sx1 - 25, py1 + 20), "32-35°C\n洗鼻安全窗\n(TRPM8关闭)", font=get_font(18), fill=(110, 231, 183))

    temps = np.linspace(10, 40, 200)
    p_norm = 1.0 / (1.0 + np.exp((temps - 21.5) / 2.2))
    p_sens = 1.0 / (1.0 + np.exp((temps - 27.5) / 2.4))

    pts_norm = [(px1 + int((t - 10) / 30.0 * (px2 - px1)), py2 - int(p * (py2 - py1 - 20))) for t, p in zip(temps, p_norm)]
    pts_sens = [(px1 + int((t - 10) / 30.0 * (px2 - px1)), py2 - int(p * (py2 - py1 - 20))) for t, p in zip(temps, p_sens)]
    draw.line(pts_norm, fill=(56, 189, 248), width=4)
    draw.line(pts_sens, fill=(244, 63, 94), width=5)

    draw.text((220, 480), "正常人阈值 (~21.5°C)", font=get_font(20), fill=(56, 189, 248))
    draw.text((460, 390), "鼻炎高敏漂移 (~27.5°C)\n微凉空气即大开水龙头！", font=get_font(20), fill=(251, 113, 133))

    draw.text((80, 815), "● 关键推论 1：冷水洗鼻 (<25°C) 会直接掉入红色高开放区，诱发反射性流涕！", font=get_font(20), fill=(248, 250, 252))
    draw.text((80, 855), "● 关键推论 2：坚持鼻喷激素 + 氮卓斯汀 12 周，可将红线左移回蓝线正常位置。", font=get_font(20), fill=(167, 243, 208))
    draw.text((80, 895), "● 关键推论 3：戴口罩将前鼻腔温度维持在 >31°C，物理锁死 TRPM8 5C-2O 门控。", font=get_font(20), fill=(125, 211, 252))

    draw.rounded_rectangle([965, 190, 1870, 985], radius=16, fill=(18, 29, 50), outline=(251, 191, 36), width=2)
    draw.text((995, 210), "模型 2：果冻涕弹黏塑性流变学与 2 小时失稳周期 (P07, P08, P10)", font=get_font(25), fill=(253, 224, 71))
    draw.text((995, 248), "储能模量 G'≈2.5 Pa > G''≈0.8 Pa | 零剪切粘度 η0≈100 Pa·s | 弛豫时间 τR≈20-40 s", font=get_font(19), fill=(148, 163, 184))

    rx1, ry1, rx2, ry2 = 1055, 310, 1815, 740
    draw.rectangle([rx1, ry1, rx2, ry2], fill=(12, 20, 36), outline=(71, 85, 105), width=2)

    crit_y = ry2 - int(0.62 * (ry2 - ry1))
    draw.rectangle([rx1 + 2, ry1 + 2, rx2 - 2, crit_y], fill=(69, 10, 26))
    draw.line([(rx1, crit_y), (rx2, crit_y)], fill=(244, 63, 94), width=3)
    draw.text((rx1 + 20, crit_y - 36), "Rayleigh-Plateau 绝对失稳阈值 (h/R >= 0.14) => 坍缩为果冻状粘液栓堵死鼻道！", font=get_font(18), fill=(253, 164, 175))

    for idx, m in enumerate([0, 30, 60, 90, 120, 150, 180]):
        gx = rx1 + int(m / 180.0 * (rx2 - rx1))
        draw.line([(gx, ry1), (gx, ry2)], fill=(30, 41, 59), width=1)
        draw.text((gx - 22, ry2 + 12), f"{m}分", font=get_font(18), fill=(148, 163, 184))
    draw.text((1330, ry2 + 45), "鼻腔黏液膜累积时间 t (分钟)", font=get_font(20), fill=(203, 213, 225))

    t_vals = np.linspace(0, 180, 200)
    h_crs = 0.03 + 0.11 * (t_vals / 120.0) ** 1.25
    pts_crs = [(rx1 + int(t / 180.0 * (rx2 - rx1)), ry2 - int(min(h, 0.21) / 0.22 * (ry2 - ry1))) for t, h in zip(t_vals, h_crs)]
    draw.line(pts_crs, fill=(251, 191, 36), width=5)

    h_rx = 0.03 + 0.04 * (1 - np.exp(-t_vals / 60.0))
    pts_rx = [(rx1 + int(t / 180.0 * (rx2 - rx1)), ry2 - int(h / 0.22 * (ry2 - ry1))) for t, h in zip(t_vals, h_rx)]
    draw.line(pts_rx, fill=(52, 211, 153), width=4)

    draw.text((1360, 490), "张益新基线：120分钟(2h)突破阈值\n冬天VIP鼻甲充血(R变窄)秒级突破！", font=get_font(20), fill=(253, 224, 71))
    draw.text((1360, 665), "温盐水+桉柠蒎+内舒拿治疗后：\n保持对流稳定薄液膜，全天无感排空", font=get_font(20), fill=(110, 231, 183))

    draw.text((995, 815), "● 为什么猛擤鼻无效且伤耳？猛擤仅 0.5s << 弛豫时间 τR(20-40s)，果冻涕纯弹性回弹！", font=get_font(20), fill=(248, 250, 252))
    draw.text((995, 855), "● 为什么果冻涕期禁用单药异丙托溴铵？关停浆液水会使果冻涕脱水硬化成坚硬鼻痂！", font=get_font(20), fill=(253, 164, 175))
    draw.text((995, 895), "● 为什么必须先洗鼻再喷药 (P09)？波浪状黏液脊会拦截 >85% 的鼻喷激素药滴！", font=get_font(20), fill=(167, 243, 208))

    out_path = os.path.join(ASSETS_DIR, "slide_03_biophysics.png")
    img.save(out_path)
    return out_path

def generate_slide_4():
    img, draw = create_base_canvas(
        "八大行业突破点 (Breakthroughs) 与八大待解决核心问题 (Open Problems)",
        "从计算流体力学数字孪生手术、AI 鼻细胞学秒级分型，到状态依赖性 TRPM8 变构药物与闭环神经调控",
        "第四幕 · 行业突破与未解难题",
        4,
    )
    left_items = [
        "★ B01 数字孪生鼻科手术规划 (P01, P02)",
        "  基于标量交换效率 E 与 Rh=1.5-2mm 均匀窄缝约束，杜绝空鼻症",
        "★ B02 智能手机显微 + AI 鼻细胞学秒级内型诊断 (P11)",
        "  YOLOv8/DETR 自动识别嗜酸/中性/杯状细胞与超微条纹 HSS",
        "★ B03 状态依赖性 TRPM8 (5C-2O) 局部变构调节剂 (P03, P04)",
        "  仅阻断病理性 O1<->O2 簇状放电，保留正常通气清凉感与体温调节",
        "★ B04 5微升床旁磁线微流变诊断芯片与靶向断键水化伴侣 (P07, P10)",
        "  30秒测定 G', η0, τy，指导二硫键裂解与钙螯合精准化胶",
        "★ B05 33.5°C 恒温闭环 + >45s 跨弛豫时间低频脉冲洗鼻站 (P10)",
        "  精确避开 TRPM8 冷激活区，温和跨越 τR=40s 彻底冲出果冻栓",
        "★ B06 呼气闭合正压 (EDS) 低 Stokes 数嗅裂/中鼻道靶向给药 (P09)",
        "★ B07 术中神经阻抗导航多点位 (中/下鼻道) PNN 冷冻/射频消融 (P16-18)",
        "★ B08 慢性鼻窦炎+神经高反应“双轨耦合”神经-免疫联合疗法",
    ]
    right_items = [
        "▶ Q01 海绵窦血管丛流固耦合 (FSI) 与非稳态蒸发相变实时仿真",
        "  突破现有刚性壁面 CFD 假设，耦合 VIP 充血动态缩窄回路",
        "▶ Q02 活体慢性炎症/酸化微环境下 TRPM8 内摩擦参数 Γ 在体测量",
        "  研发门诊内镜下微电极三叉神经黏膜诱发电位定量测评仪",
        "▶ Q03 弹黏塑性果冻涕在 1.5mm 窦口狭缝中的非线性毛细架桥与解聚",
        "  将非牛顿 EVP 本构代入 Hazra-Picardo 薄膜失稳方程求解",
        "▶ Q04 抗胆碱能控水 (M3阻断) 与 7μm 纤毛液层 (PCL) 润滑的最优平衡",
        "  建立基于黏液初始模量 G'0 的部分受体占有率剂量控制方程",
        "▶ Q05 嗅裂微息肉对嗅觉-三叉神经化学感觉耦合的可逆性时间窗",
        "▶ Q06 牙源性上颌窦炎、真菌球与 2型嗜酸性鼻窦炎的无创多模态早筛",
        "▶ Q07 PNN 消融术后 1-3 年轴突再生表型重编程与可逆生物电子接口",
        "▶ Q08 个体化“气象温湿度预警-洗鼻温控-12周依从性”数字疗法闭环",
    ]
    draw_card(draw, [50, 190, 945, 985], "八大前沿行业突破点 (8 Industry Breakthroughs)", left_items, (56, 189, 248))
    draw_card(draw, [975, 190, 1870, 985], "亟待继续攻克的八大科学工程问题 (8 Open Problems)", right_items, (168, 85, 247))

    out_path = os.path.join(ASSETS_DIR, "slide_04_breakthroughs.png")
    img.save(out_path)
    return out_path

def generate_slide_5():
    img, draw = create_base_canvas(
        "张益新（20年病程）“双轨叠加型”精准诊断清单与四阶梯治疗全案",
        "底盘：双侧上颌窦/左筛窦炎 + 左嗅裂荔肉样突起 + 2h果冻涕 | 放大器：左利特尔区糜烂 + 冬季 TRPM8 秒级高敏",
        "第五幕 · 张益新个体化诊疗方案",
        5,
    )
    diag_items = [
        "● 客观基线：2024 MRI & 2025.11.15 同济CT/内镜证实双侧上颌窦炎、",
        "  鼻中隔左偏、双下/中鼻甲肥大、左嗅裂荔肉样光滑突起、左利特尔区糜烂",
        "★ 必查拼图 1【查内型】：鼻分泌物涂片细胞学 (查嗜酸/中性/杯状细胞)",
        "  + 血常规嗜酸性粒细胞绝对值 (EOS#) + 血清总 IgE & 特异性 sIgE",
        "  (结合既往激素秒效型肛周湿疹，高度提示 2 型嗜酸性炎症，激素极敏感)",
        "★ 必查拼图 2【查牙源】：口腔牙周科洁治 + 上后牙小视野 CBCT",
        "  (排查上磨牙黑锈色结石/根尖周炎穿透上颌窦底壁导致的黄白黏涕与口臭)",
        "★ 必查拼图 3【查CT细节】：复盘 2025.11.15 CT 骨窗 OMC 宽度与钙化点",
        "★ 必查拼图 4【查耳咽管】：声导抗 (Tympanometry) + 鼻呼出气 NO (FnNO)",
        "● 终身用药红线：绝对禁用左氧氟沙星/莫西沙星等一切喹诺酮类抗生素！",
    ]
    rx_items = [
        "★ 第一阶梯（每日基石）：33.5°C 弱碱性缓冲盐水 240mL 洗鼻 (早晚各1次)",
        "  单侧温和冲洗 >=45-60s (跨越 τR=40s 弛豫时间)，严禁猛擤鼻与挖鼻；",
        "  冬季出门必戴保暖口罩；左利特尔区糜烂点浅涂透明质酸凝胶护创。",
        "★ 第二阶梯（12周规范靶向药，严格执行【先洗鼻 -> 隔15分 -> 后喷药】）：",
        "  ① 爱赛平 (氮卓斯汀鼻喷)：早晚每侧 1 喷 => 脱敏 TRPM8 & 抑 VIP/鼻后滴漏",
        "  ② 内舒拿 (糠酸莫米松)：洗鼻后每侧 2 喷 => 消除左嗅裂突起与鼻窦水肿",
        "     【喷鼻铁律】左手喷右鼻、右手喷左鼻朝外眼角，喷后低头前倾浸润嗅裂！",
        "  ③ 切诺 (桉柠蒎肠溶胶囊)：前2-4周餐前30分凉温水吞服 => 水化破除果冻涕",
        "  ④ 异丙托溴铵：平时果冻涕期禁用！仅限冬日寒风出门前15分钟按需控清水",
        "★ 第三/四阶梯（第4周&12周复盘）：满12周内镜复查左嗅裂突起；若残留",
        "  顽固结构或反射，行保留鼻甲 CFD 导航 Mini-FESS + 后鼻神经微创冷冻消融。",
    ]
    draw_card(draw, [50, 190, 935, 985], "精准诊断方案：补齐 20 年病历的 4 块关键拼图", diag_items, (245, 158, 11))
    draw_card(draw, [965, 190, 1870, 985], "四阶梯治疗方案：水化破胶 + 神经脱敏 + 嗅裂抗炎", rx_items, (16, 185, 129))

    out_path = os.path.join(ASSETS_DIR, "slide_05_treatment.png")
    img.save(out_path)
    return out_path

NARRATIONS = [
    (
        "slide_01_6w2h.png",
        "欢迎观看鼻腔生物物理与精准鼻科学深度综述。第一幕：解码冷空气30秒流涕的6W2H机制。你流出的白色清涕不是发炎脓涕，而是98%的水、电解质与少量黏蛋白。发表于PNAS与流体力学的论文证明，人类鼻腔容积仅21立方厘米，比同体型哺乳动物缩减了90%，前三分之一鼻腔在1.5毫米的极窄缝隙内承担了80%的加温加湿负荷，蒸发冷却热通量高达每平方米15.6瓦。黏膜降温在毫秒级激活三叉神经TRPM8冷觉探头，信号经脑干上泌涎核与翼腭神经节换元，通过后鼻神经释放乙酰胆碱和血管活性肠肽，驱动9万个黏膜下腺与200多个前部浆液腺在10到30秒内开闸放水。",
    ),
    (
        "slide_02_18papers.png",
        "第二幕：18篇跨学科核心论文的十遍精读图谱。我们将11篇arXiv物理学与人工智能论文，以及7篇Europe PMC临床权威文献分为四大集群：集群A定量了鼻腔狭缝标量交换效率与蒸发冷却震中；集群B揭示了TRPM8通道5闭2开的七态马尔可夫拓扑，以及蛋白质内摩擦激活能倒置带来的Q10等于100超敏冷激活；集群C通过磁线主动微流变学与薄膜润滑方程，阐明了黏液凝胶的毛细失稳相变；集群D结合深度学习鼻细胞学与472例患者的Meta分析，确立了非过敏性鼻病与后鼻神经冷冻消融的循证闭环。",
    ),
    (
        "slide_03_biophysics.png",
        "第三幕：核心生物物理定量模型。左图展示了TRPM8开放概率随温度的陡峭变化：慢性炎症与黏膜糜烂使半激活电压向高温漂移，导致微凉空气甚至低于25度的冷水洗鼻都会直接触发簇状放电；唯有32至35摄氏度的温盐水与保暖口罩能将通道锁定在安全关闭窗。右图揭示了为什么张益新每隔2小时鼻腔就会被果冻涕堵满：呼吸道黏液零剪切粘度是水的10万倍，应力弛豫时间长达20到40秒。仅持续半秒的用力猛擤只会引发纯弹性回弹并伤及咽鼓管；而且在果冻涕期绝不能单用异丙托溴铵，否则关停水分会导致黏液干涸结痂。",
    ),
    (
        "slide_04_breakthroughs.png",
        "第四幕：八大行业突破点与八大待解决科学工程问题。基于18篇文献，未来耳鼻喉科正迎来八大突破：包括预防空鼻症的数字孪生CFD手术导航、智能手机1分钟AI鼻细胞学内型诊断、只阻断双开态簇状放电的TRPM8局部变构调节剂、5微升床旁黏液微流变芯片、33.5度恒温跨弛豫时间脉冲洗鼻站、呼气闭合正压嗅裂靶向给药，以及术中神经阻抗导航的多点位后鼻神经消融。同时，海绵窦血管丛流固耦合仿真、活体TRPM8内摩擦参数测定、以及牙源性与2型嗜酸性鼻窦炎的无创早筛，仍是亟待继续攻克的科学前沿。",
    ),
    (
        "slide_05_treatment.png",
        "第五幕：针对张益新20年病程的双轨机制精准诊断与四阶梯治疗方案。你的鼻炎是A轨慢性鼻窦炎果冻涕底盘，叠加B轨冷空气神经反射放大器。诊断上需补齐四块拼图：鼻分泌物涂片细胞学与血嗜酸性粒细胞、口腔科上后牙CBCT排查牙源性上颌窦炎、CT骨窗复盘以及声导抗测试，并终身禁用喹诺酮类抗生素。治疗上严格执行四阶梯法则：每天早晚用33.5度弱碱性缓冲盐水温和冲洗60秒以上破除果冻栓，静置15分钟后先喷氮卓斯汀脱敏神经反射，再按交叉朝外眼角方向喷糠酸莫米松消除左嗅裂荔肉样突起，配合桉柠蒎促排，满12周复盘内镜。",
    ),
]

def build_video():
    print("Generating 5 high-res slides...")
    generate_slide_1()
    generate_slide_2()
    generate_slide_3()
    generate_slide_4()
    generate_slide_5()

    segment_files = []
    tmp_dir = os.path.join(ASSETS_DIR, "tmp_video")
    os.makedirs(tmp_dir, exist_ok=True)

    for idx, (slide_name, text) in enumerate(NARRATIONS, 1):
        slide_path = os.path.join(ASSETS_DIR, slide_name)
        aiff_path = os.path.join(tmp_dir, f"seg_{idx:02d}.aiff")
        seg_mp4 = os.path.join(tmp_dir, f"seg_{idx:02d}.mp4")

        print(f"Synthesizing TTS audio for scene {idx}...")
        subprocess.run(
            ["say", "-v", "Tingting", "-r", "195", "-o", aiff_path, text],
            check=True,
        )

        print(f"Encoding video segment {idx}...")
        subprocess.run(
            [
                "/Users/yixin0909zhang/miniconda3/bin/ffmpeg",
                "-y",
                "-loop", "1",
                "-i", slide_path,
                "-i", aiff_path,
                "-c:v", "libx264",
                "-tune", "stillimage",
                "-c:a", "aac",
                "-b:a", "192k",
                "-pix_fmt", "yuv420p",
                "-shortest",
                "-vf", "scale=1920:1080",
                seg_mp4,
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        segment_files.append(seg_mp4)

    concat_list = os.path.join(tmp_dir, "concat.txt")
    with open(concat_list, "w", encoding="utf-8") as f:
        for seg in segment_files:
            f.write(f"file '{seg}'\n")

    final_mp4 = os.path.join(ASSETS_DIR, "rhinitis_6w2h_review_video.mp4")
    print("Concatenating segments into final MP4...")
    subprocess.run(
        [
            "/Users/yixin0909zhang/miniconda3/bin/ffmpeg",
            "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", concat_list,
            "-c", "copy",
            final_mp4,
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # Clean up temporary segments
    for seg in segment_files:
        if os.path.exists(seg):
            os.remove(seg)
    for idx in range(1, 6):
        ap = os.path.join(tmp_dir, f"seg_{idx:02d}.aiff")
        if os.path.exists(ap):
            os.remove(ap)
    if os.path.exists(concat_list):
        os.remove(concat_list)
    if os.path.exists(tmp_dir):
        os.rmdir(tmp_dir)

    print(f"Successfully generated video: {final_mp4}")

if __name__ == "__main__":
    build_video()
