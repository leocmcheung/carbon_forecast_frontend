import streamlit as st
import pandas as pd
import joblib
import os
from PIL import Image
import time
st.set_page_config(page_title="GreenWagon: Tackling Global Warming Step by Step", page_icon="images/green-wagon.png", layout="wide", initial_sidebar_state="auto", menu_items=None)
cs_img = Image.open(os.path.abspath("images/climate-care.png"))
# st.image(cs_img,width=imgwidth)
st.title("Find your company's climate strategy score")

sector_list = ('','Communication Services',
 'Consumer Discretionary',
 'Consumer Staples',
 'Energy',
 'Financials',
 'Health Care',
 'Industrials',
 'Information Technology',
 'Materials',
 'Real Estate',
 'Utilities')
secrev_list = ( '', 'Abrasive product manufacturing',
 'Accounting, tax preparation, bookkeeping, and payroll services',
 'Adhesive manufacturing',
 'Advertising and related services',
 'Air and gas compressor manufacturing',
 'Air conditioning, refrigeration, and warm air heating equipment manufacturing',
 'Air purification and ventilation equipment manufacturing',
 'Air transportation',
 'Aircraft engine and engine parts manufacturing',
 'Aircraft manufacturing',
 'Alkalies and chlorine manufacturing',
 'All other basic inorganic chemical manufacturing',
 'All other chemical product and preparation manufacturing',
 'All other converted paper product manufacturing',
 'All other crop farming',
 'All other food manufacturing',
 'All other forging, stamping, and sintering',
 'All other miscellaneous electrical equipment and component manufacturing',
 'All other miscellaneous manufacturing',
 'All other miscellaneous professional, scientific, and technical services',
 'All other miscellaneous wood product manufacturing',
 'All other paper bag and coated and treated paper manufacturing',
 'All other petroleum and coal products manufacturing',
 'All other textile product mills',
 'All other transportation equipment manufacturing',
 'Alumina refining and primary aluminum production',
 'Aluminum product manufacturing from purchased aluminum',
 'Ammunition manufacturing',
 'Amusement parks, arcades, and gambling industries',
 'Analytical laboratory instrument manufacturing',
 'Animal (except poultry) slaughtering, rendering, and processing',
 'Animal production, except cattle and poultry and eggs',
 'Apparel accessories and other apparel manufacturing',
 'Apparel knitting mills',
 'Apparel, Piece Goods, and Notions Wholesalers',
 'Architectural, engineering, and related services',
 'Arms, ordnance, and accessories manufacturing',
 'Artificial and synthetic fibers and filaments manufacturing',
 'Asphalt paving mixture and block manufacturing',
 'Asphalt shingle and coating materials manufacturing',
 'Audio and video equipment manufacturing',
 'Automatic environmental control manufacturing',
 'Automobile manufacturing',
 'Automotive equipment rental and leasing',
 'Automotive repair and maintenance, except car washes',
 'Ball and roller bearing manufacturing',
 'Bare printed circuit board manufacturing',
 'Bauxite Mining',
 'Beet sugar manufacturing',
 'Biological product (except diagnostic) manufacturing',
 'Biomass Power Generation',
 'Bituminous Coal Underground Mining',
 'Bituminous Coal and Lignite Surface Mining',
 'Blind and shade manufacturing',
 'Boat building',
 'Book publishers',
 'Bowling centers',
 'Bread and bakery product manufacturing',
 'Breakfast cereal manufacturing',
 'Breweries',
 'Brick, tile, and other structural clay product manufacturing',
 'Broadcast and wireless communications equipment',
 'Broadwoven fabric mills',
 'Broom, brush, and mop manufacturing',
 'Building Material and Garden Equipment and Supplies Dealers',
 'Business support services',
 'Cable and other subscription programming',
 'Car washes',
 'Carbon and graphite product manufacturing',
 'Carbon black manufacturing',
 'Carpet and rug mills',
 'Cattle ranching and farming',
 'Cement manufacturing',
 'Cheese manufacturing',
 'Child day care services',
 'Chocolate and confectionery manufacturing from cacao beans',
 'Clay and nonclay refractory manufacturing',
 'Clothing and Clothing Accessories Stores',
 'Coal Power Generation',
 'Coated and laminated paper, packaging paper and plastics film manufacturing',
 'Coating, engraving, heat treating and allied activities',
 'Coffee and tea manufacturing',
 'Commercial and industrial machinery and equipment rental and leasing',
 'Commercial and industrial machinery and equipment repair and maintenance',
 'Communication and energy wire and cable manufacturing',
 'Community food, housing, and other relief services, including rehabilitation services',
 'Computer storage device manufacturing',
 'Computer systems design services',
 'Computer terminals and other computer peripheral equipment manufacturing',
 'Concrete pipe, brick, and block manufacturing',
 'Confectionery manufacturing from purchased chocolate',
 'Construction machinery manufacturing',
 'Cookie, cracker, and pasta manufacturing',
 'Copper Mining',
 'Copper rolling, drawing, extruding and alloying',
 'Cotton farming',
 'Couriers and messengers',
 'Crown and closure manufacturing and metal stamping',
 'Crude Petroleum and Natural Gas Extraction',
 'Curtain and linen mills',
 'Custom architectural woodwork and millwork manufacturing',
 'Custom computer programming services',
 'Cut and sew apparel contractors',
 'Cut stone and stone product manufacturing',
 'Cutlery, utensil, pot, and pan manufacturing',
 'Cutting tool and machine tool accessory manufacturing',
 'Dairy cattle and milk production',
 'Data processing, hosting, and related services',
 'Death care services',
 'Dental equipment and supplies manufacturing',
 'Directory, mailing list, and other publishers',
 'Distilleries',
 'Dog and cat food manufacturing',
 'Doll, toy, and game manufacturing',
 'Drilling oil and gas wells',
 'Dry, condensed, and evaporated dairy product manufacturing',
 'Dry-cleaning and laundry services',
 'Electric Bulk Power Transmission and Control',
 'Electric Power Distribution',
 'Electric lamp bulb and part manufacturing',
 'Electrical and Electronic Goods Wholesalers',
 'Electricity and signal testing instruments manufacturing',
 'Electromedical and electrotherapeutic apparatus manufacturing',
 'Electron tube manufacturing',
 'Electronic and precision equipment repair and maintenance',
 'Electronic capacitor, resistor, coil, transformer, and other inductor manufacturing',
 'Electronic computer manufacturing',
 'Electronic connector manufacturing',
 'Electronics and Appliance Stores',
 'Elementary and secondary schools',
 'Employment services',
 'Engineered wood member and truss manufacturing',
 'Environmental and other technical consulting services',
 'Fabric coating mills',
 'Fabricated pipe and pipe fitting manufacturing',
 'Facilities support services',
 'Farm machinery and equipment manufacturing',
 'Fats and oils refining and blending',
 'Ferrous metal foundries',
 'Fertilizer manufacturing',
 'Fiber, yarn, and thread mills',
 'Fishing',
 'Fitness and recreational sports centers',
 'Flat glass manufacturing',
 'Flavoring syrup and concentrate manufacturing',
 'Flour milling and malt manufacturing',
 'Fluid milk and butter manufacturing',
 'Fluid power process machinery',
 'Food services and drinking places',
 'Food, Beverage, Health, and Personal Care Stores',
 'Footwear manufacturing',
 'Forest nurseries, forest products, and timber tracts',
 'Frozen food manufacturing',
 'Fruit and vegetable canning, pickling, and drying',
 'Fruit farming',
 'Funds, trusts, and other financial vehicles',
 'Furniture and Home Furnishings Stores',
 'Gasket, packing, and sealing device manufacturing',
 'Gasoline Stations',
 'General Merchandise Stores',
 'General and consumer goods rental except video tapes and discs',
 'Geothermal Power Generation',
 'Glass container manufacturing',
 'Glass product manufacturing made of purchased glass',
 'Gold Ore Mining',
 'Grain farming',
 'Grantmaking, giving, and social advocacy organizations',
 'Greenhouse, nursery, and floriculture production',
 'Grocery and Related Product Wholesalers',
 'Ground or treated mineral and earth manufacturing',
 'Guided missile and space vehicle manufacturing',
 'Handtool manufacturing',
 'Hardware manufacturing',
 'Heating equipment (except warm air furnaces) manufacturing',
 'Heavy duty truck manufacturing',
 'Home health care services',
 'Hospitals',
 'Hotels and motels, including casino hotels',
 'Household cooking appliance manufacturing',
 'Household laundry equipment manufacturing',
 'Household refrigerator and home freezer manufacturing',
 'Hydroelectric Power Generation',
 'Ice cream and frozen dessert manufacturing',
 'In-vitro diagnostic substance manufacturing',
 'Independent artists, writers, and performers',
 'Individual and family services',
 'Industrial gas manufacturing',
 'Industrial mold manufacturing',
 'Industrial process furnace and oven manufacturing',
 'Industrial process variable instruments manufacturing',
 'Institutional furniture manufacturing',
 'Insurance agencies, brokerages, and related activities',
 'Insurance carriers',
 'Internet publishing and broadcasting',
 'Internet service providers and web search portals',
 'Investigation and security services',
 'Iron and steel mills and ferroalloy manufacturing',
 'Iron ore mining',
 'Irradiation apparatus manufacturing',
 'Jewelry and silverware manufacturing',
 'Junior colleges, colleges, universities, and professional schools',
 'Knit fabric mills',
 'Laminated plastics plate, sheet (except packaging), and shape manufacturing',
 'Landfill Gas Power Generation',
 'Lawn and garden equipment manufacturing',
 'Lead Ore and Zinc Ore Mining',
 'Leather and hide tanning and finishing',
 'Legal services',
 'Lessors of nonfinancial intangible assets',
 'Light truck and utility vehicle manufacturing',
 'Lighting fixture manufacturing',
 'Lime and gypsum product manufacturing',
 'Logging',
 'Lumber and Other Construction Materials Wholesalers',
 'Magnetic and optical recording media manufacturing',
 'Management of companies and enterprises',
 'Management, scientific, and technical consulting services',
 'Manufactured home (mobile home) manufacturing',
 'Material handling equipment manufacturing',
 'Mattress manufacturing',
 'Mechanical power transmission equipment manufacturing',
 'Medical and diagnostic labs and outpatient and other ambulatory care services',
 'Medicinal and botanical manufacturing',
 "Men's and boys' cut and sew apparel manufacturing",
 'Metal and other household furniture manufacturing',
 'Metal can, box, and other metal container (light gauge) manufacturing',
 'Metal cutting and forming machine tool manufacturing',
 'Metal tank (heavy gauge) manufacturing',
 'Military armored vehicle, tank, and tank component manufacturing',
 'Mineral wool manufacturing',
 'Mining and oil and gas field machinery manufacturing',
 'Miscellaneous Durable Goods Wholesalers',
 'Miscellaneous Nondurable Goods Wholesalers',
 'Miscellaneous Store Retailers',
 'Miscellaneous nonmetallic mineral products',
 'Monetary authorities and depository credit intermediation',
 'Motion picture and video industries',
 'Motor Vehicle and Machinery, Equipment, and Supplies Wholesalers',
 'Motor Vehicle and Parts Dealers',
 'Motor and generator manufacturing',
 'Motor home manufacturing',
 'Motor vehicle body manufacturing',
 'Motor vehicle parts manufacturing',
 'Motorcycle, bicycle, and parts manufacturing',
 'Museums, historical sites, zoos, and parks',
 'Musical instrument manufacturing',
 'Narrow fabric mills and schiffli machine embroidery',
 'Natural Gas Liquid Extraction',
 'Natural Gas Power Generation',
 'Natural gas distribution',
 'Newspaper publishers',
 'Nickel Mining',
 'Nonchocolate confectionery manufacturing',
 'Nondepository credit intermediation and related activities',
 'Nonferrous metal (except copper and aluminum) rolling, drawing, extruding and alloying',
 'Nonferrous metal foundries',
 'Nonresidential commercial and health care structures',
 'Nonresidential maintenance and repair',
 'Nonresidential manufacturing structures',
 'Nonstore Retailers',
 'Nonupholstered wood household furniture manufacturing',
 'Nonwoven fabric mills',
 'Nuclear Electric Power Generation',
 'Nursing and residential care facilities',
 'Office administrative services',
 'Office furniture manufacturing',
 'Office supplies (except paper) manufacturing',
 'Offices of physicians, dentists, and other health practitioners',
 'Oilseed farming',
 'Ophthalmic goods manufacturing',
 'Optical instrument and lens manufacturing',
 'Ornamental and architectural metal products manufacturing',
 'Other Electric Power Generation',
 'Other Metal Ore Mining',
 'Other accommodations',
 'Other aircraft parts and auxiliary equipment manufacturing',
 'Other amusement and recreation industries',
 'Other animal food manufacturing',
 'Other basic organic chemical manufacturing',
 'Other commercial and service industry machinery manufacturing',
 'Other communications equipment manufacturing',
 'Other computer related services, including facilities management',
 'Other concrete product manufacturing',
 'Other cut and sew apparel manufacturing',
 'Other educational services',
 'Other electronic component manufacturing',
 'Other engine equipment manufacturing',
 'Other fabricated metal manufacturing',
 'Other general purpose machinery manufacturing',
 'Other industrial machinery manufacturing',
 'Other information services',
 'Other leather and allied product manufacturing',
 'Other major household appliance manufacturing',
 'Other nonmetallic mineral mining and quarrying',
 'Other nonresidential structures',
 'Other personal services',
 'Other plastics product manufacturing',
 'Other pressed and blown glass and glassware manufacturing',
 'Other residential structures',
 'Other rubber product manufacturing',
 'Other support services',
 'Packaging machinery manufacturing',
 'Paint and coating manufacturing',
 'Paper mills',
 'Paperboard Mills',
 'Paperboard container manufacturing',
 'Performing arts companies',
 'Periodical publishers',
 'Personal and household goods repair and maintenance',
 'Personal care services',
 'Pesticide and other agricultural chemical manufacturing',
 'Petrochemical manufacturing',
 'Petroleum Power Generation',
 'Petroleum lubricating oil and grease manufacturing',
 'Petroleum refineries',
 'Petroleum, Chemical, and Allied Products Wholesalers',
 'Pharmaceutical preparation manufacturing',
 'Photographic and photocopying equipment manufacturing',
 'Photographic services',
 'Pipeline transportation',
 'Plastics and rubber industry machinery manufacturing',
 'Plastics bottle manufacturing',
 'Plastics material and resin manufacturing',
 'Plastics packaging materials and unlaminated film and sheet manufacturing',
 'Plastics pipe and pipe fitting manufacturing',
 'Plate work and fabricated structural product manufacturing',
 'Plumbing fixture fitting and trim manufacturing',
 'Polystyrene foam product manufacturing',
 'Postal service',
 'Pottery, ceramics, and plumbing fixture manufacturing',
 'Poultry and egg production',
 'Poultry processing',
 'Power boiler and heat exchanger manufacturing',
 'Power, distribution, and specialty transformer manufacturing',
 'Power-driven handtool manufacturing',
 'Prefabricated wood building manufacturing',
 'Primary battery manufacturing',
 'Primary smelting and refining of copper',
 'Primary smelting and refining of nonferrous metal (except copper and aluminum)',
 'Printed circuit assembly (electronic assembly) manufacturing',
 'Printing',
 'Printing ink manufacturing',
 'Promoters of performing arts and sports and agents for public figures',
 'Propulsion units and parts for space vehicles and guided missiles',
 'Pulp mills',
 'Pump and pumping equipment manufacturing',
 'Radio and television broadcasting',
 'Rail transportation (Diesel)',
 'Rail transportation (Electric)',
 'Railroad rolling stock manufacturing',
 'Ready-mix concrete manufacturing',
 'Real estate',
 'Reconstituted wood product manufacturing',
 'Relay and industrial control manufacturing',
 'Residential maintenance and repair',
 'Residential permanent site single- and multi-family structures',
 'Rolling mill and other metalworking machinery manufacturing',
 'Rubber and plastics hoses and belting manufacturing',
 'Sand, gravel, clay, and ceramic and refractory minerals mining and quarrying',
 'Sanitary paper product manufacturing',
 'Sawmills and wood preservation',
 'Scientific research and development services',
 'Seafood product preparation and packaging',
 'Search, detection, and navigation instruments manufacturing',
 'Seasoning and dressing manufacturing',
 'Secondary smelting and alloying of aluminum',
 'Securities, commodity contracts, investments, and related activities',
 'Semiconductor and related device manufacturing',
 'Semiconductor machinery manufacturing',
 'Services to buildings and dwellings',
 'Ship building and repairing',
 'Showcase, partition, shelving, and locker manufacturing',
 'Sign manufacturing',
 'Small electrical appliance manufacturing',
 'Snack food manufacturing',
 'Soap and cleaning compound manufacturing',
 'Soft drink and ice manufacturing',
 'Software publishers',
 'Software, audio, and video media reproducing',
 'Solar Power Generation',
 'Sound recording industries',
 'Soybean and other oilseed processing',
 'Special tool, die, jig, and fixture manufacturing',
 'Specialized design services',
 'Spectator sports',
 'Speed changer, industrial high-speed drive, and gear manufacturing',
 'Sporting and athletic goods manufacturing',
 'Spring and wire product manufacturing',
 'Stationery product manufacturing',
 'Steel product manufacturing from purchased steel',
 'Stone mining and quarrying',
 'Storage battery manufacturing',
 'Sugar cane mills and refining',
 'Sugarcane and sugar beet farming',
 'Support activities for agriculture and forestry',
 'Support activities for oil and gas operations',
 'Support activities for other mining',
 'Support activities for printing',
 'Support activities for transportation',
 'Surgical and medical instrument manufacturing',
 'Surgical appliance and supplies manufacturing',
 'Switchgear and switchboard apparatus manufacturing',
 'Synthetic dye and pigment manufacturing',
 'Synthetic rubber manufacturing',
 'Tar Sands Extraction',
 'Telecommunications',
 'Telephone apparatus manufacturing',
 'Textile and fabric finishing mills',
 'Textile bag and canvas mills',
 'Tire manufacturing',
 'Tobacco product manufacturing',
 'Toilet preparation manufacturing',
 'Totalizing fluid meters and counting devices manufacturing',
 'Transit and ground passenger transportation',
 'Travel arrangement and reservation services',
 'Travel trailer and camper manufacturing',
 'Tree nut farming',
 'Truck trailer manufacturing',
 'Truck transportation',
 'Turbine and turbine generator set units manufacturing',
 'Turned product and screw, nut, and bolt manufacturing',
 'Unlaminated plastics profile shape manufacturing',
 'Upholstered household furniture manufacturing',
 'Uranium-Radium-Vanadium Ore Mining',
 'Urethane and other foam product (except polystyrene) manufacturing',
 'Valve and fittings other than plumbing',
 'Vegetable and melon farming',
 'Vending, commercial, industrial, and office machinery manufacturing',
 'Veneer and plywood manufacturing',
 'Veterinary services',
 'Warehousing and storage',
 'Waste management and remediation services',
 'Watch, clock, and other measuring and controlling device manufacturing',
 'Water transportation',
 'Water, sewage and other systems',
 'Wave & Tidal Power Generation',
 'Wet corn milling',
 'Wind Power Generation',
 'Wineries',
 'Wiring device manufacturing',
 "Women's and girls' cut and sew apparel manufacturing",
 'Wood container and pallet manufacturing',
 'Wood kitchen cabinet and countertop manufacturing',
 'Wood windows and doors and millwork')
CSS = """

.css-1bim6c1{
    font-size:20px;
}
.st-af{
    font-size:18px;
}
.css-1inwz65{
    font-size:18px;
}
.css-17ogifi{
    font-size:18px;
    top:-28px;
}
[data-baseweb="select"] {
    font-size:20px;
    }
.st-c5.st-ci.st-cj.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-ck.st-cl{
    font-size:14px;
}
.css-50ug3q{
    font-size:30px;
}
.css-nojwjo{
    font-size:26px;
}
.score_cls{
    color:firebrick;
    font-size:96px;
    text-align: center;
}
.css-6nj7z3{
    font-size:26px;
}
.css-th66yb{
    font-size:24px;
}
.css-1ec096l{
    margin-left:-150px;
    margin-right: -150px
}
.benmk{
    font-style: italic;
    color:DarkSlateGrey
}
"""


st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)




hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''

st.markdown(hide_img_fs, unsafe_allow_html=True)
with st.sidebar.container():
    for i in range(25):
        st.write("")
    st.image("images/green-wagon.png")

imgwidth=66
preset = st.radio("Preset Portfolios", ("A Financials company","An Industrial company", "A Health Care company", "Custom"), index=3)
col1, col1img, col2, col2img,col3 = st.columns([15,3,17,3,8])



if preset == "A Financials company":
    sector_pre = 5
    revenue_pre = 3000
    employees_pre = 40000
    secrev1_pre =149
    secrev2_pre = 194
    secrev3_pre = 234
    secrevpc1_pre = 60
    secrevpc2_pre = 27
elif preset == "An Industrial company":
    sector_pre = 7
    revenue_pre = 30000
    employees_pre = 25000
    secrev1_pre =3
    secrev2_pre = 318
    secrev3_pre = 400
    secrevpc1_pre = 40
    secrevpc2_pre = 30
elif preset == "A Health Care company":
    sector_pre = 6
    revenue_pre = 40000
    employees_pre = 25000
    secrev1_pre =317
    secrev2_pre = 401
    secrev3_pre = 400
    secrevpc1_pre = 90
    secrevpc2_pre = 5
else:
    sector_pre = 0
    revenue_pre = 0
    employees_pre = 0
    secrev1_pre =0
    secrev2_pre = 0
    secrev3_pre = 0
    secrevpc1_pre = 34
    secrevpc2_pre = round((100-secrevpc1_pre)/2)

with col1:
    sector = st.selectbox("Company sector:",
                sector_list, index=sector_pre, help="What is your company's GCIS Sector?")
    revenue = st.number_input('Annual revenue ($mn)', value=revenue_pre)
    employees = st.number_input('Number of employees', value=employees_pre, step=10)

with col1img:
    sec_img = Image.open(os.path.abspath("images/company.png"))
    st.image(sec_img, width=imgwidth)
    st.text("")
    st.text("")
    rev_img = Image.open(os.path.abspath("images/sales-performance--v5.png"))
    st.image(rev_img, width=imgwidth)
    st.text("")
    emp_img = Image.open(os.path.abspath("images/business-conference-female-speaker--v1.png"))
    st.image(emp_img,width=imgwidth)
with col2:
    secrev1 = st.selectbox('Sector revenue #1',secrev_list, index=secrev1_pre)
    secrev2 = st.selectbox('Sector revenue #2',secrev_list, index=secrev2_pre)
    secrev3 = st.selectbox('Sector revenue #3',secrev_list, index=secrev3_pre)
with col2img:
    sec1_img = Image.open(os.path.abspath("images/tree-structure.png"))
    st.image(sec1_img, width=imgwidth)
    st.text("")
    st.text("")
    sec2_img = Image.open(os.path.abspath("images/tree-structure.png"))
    st.image(sec2_img, width=imgwidth)
    st.text("")
    st.text("")
    sec3_img = Image.open(os.path.abspath("images/tree-structure.png"))
    st.image(sec3_img,width=imgwidth)
with col3:
    secrev_pc1 = st.slider("Percentage:", 0, 100, secrevpc1_pre, key="secrev001")
    secrev_pc2 = st.slider("Percentage:", 0, 100, secrevpc2_pre, key="secrev002")
    secrev_pc3 = st.slider("Percentage:", 0, 100, 100-secrev_pc1-secrev_pc2 , key="secrev003")

# if sector == "Energy":
#     st.write("(For energy companies only) Revenue % for:")
#     col1,col2,col3,col4,col5,col6,col7 = st.columns(7)
#     with col1:
#         arc_rev = st.number_input("Arctic Drilling %:",step=1.)
#     with col2:
#         coal_rev = st.number_input("Coal %:",step=1.)
#     with col3:
#         nuc_rev = st.number_input("Nuclear %:",step=1.)
#     with col4:
#         oil_rev = st.number_input("Oil & Sands %:",step=1.)
#     with col5:
#         shale_rev = st.number_input("Shale Oil & Gas %:",step=1.)
#     with col6:
#         uds_rev = st.number_input("Ultra Deep Sea Drilling %:",step=1.)
#     with col7:
#         thr_rev = st.number_input("Thermal Coal %:")
#     st.write("Total input % =", round(arc_rev +coal_rev+nuc_rev+oil_rev+shale_rev+uds_rev+thr_rev,2))
#     if arc_rev +coal_rev+nuc_rev+oil_rev+shale_rev+uds_rev+thr_rev > 100:
#         pow_rev_warn = '<p style="color:Red; font-size: 14px;">Total Revenue % should not be over 100% :)</p>'
#         st.markdown(pow_rev_warn, unsafe_allow_html=True)
#         ene_err = True

X=pd.DataFrame({'Sector':[sector],
 'Employees / Revenue':employees/revenue if revenue!=0 else 0.,
 'revenue':revenue,
 'nuclear_percentage_revenue':0.,#nuc_rev  if sector == "Energy" else 0.,
 'thermal_coal_percentage_revenue':0.,#thr_rev if sector == "Energy" else 0.,
 'ultra_deep_sea_drilling_percentage_revenue':0.,#uds_rev  if sector == "Energy" else 0.,
 'shale_oil_gas_percentage_revenue':0.,#shale_rev  if sector == "Energy" else 0.,
 'coal_percentage_revenue':0.,#coal_rev  if sector == "Energy" else 0.,
 'arctic_drilling_percentage_revenue':0.,#arc_rev if sector == "Energy" else 0.,
 'oil_sands_percentage_revenue':0.,#oil_rev if sector == "Energy" else 0.,
 'Abrasive product manufacturing':0.,
 'Accounting, tax preparation, bookkeeping, and payroll services':0.,
 'Adhesive manufacturing':0.,
 'Advertising and related services':0.,
 'Air and gas compressor manufacturing':0.,
 'Air conditioning, refrigeration, and warm air heating equipment manufacturing':0.,
 'Air purification and ventilation equipment manufacturing':0.,
 'Air transportation':0.,
 'Aircraft engine and engine parts manufacturing':0.,
 'Aircraft manufacturing':0.,
 'Alkalies and chlorine manufacturing':0.,
 'All other basic inorganic chemical manufacturing':0.,
 'All other chemical product and preparation manufacturing':0.,
 'All other converted paper product manufacturing':0.,
 'All other crop farming':0.,
 'All other food manufacturing':0.,
 'All other forging, stamping, and sintering':0.,
 'All other miscellaneous electrical equipment and component manufacturing':0.,
 'All other miscellaneous manufacturing':0.,
 'All other miscellaneous professional, scientific, and technical services':0.,
 'All other miscellaneous wood product manufacturing':0.,
 'All other paper bag and coated and treated paper manufacturing':0.,
 'All other petroleum and coal products manufacturing':0.,
 'All other textile product mills':0.,
 'All other transportation equipment manufacturing':0.,
 'Alumina refining and primary aluminum production':0.,
 'Aluminum product manufacturing from purchased aluminum':0.,
 'Ammunition manufacturing':0.,
 'Amusement parks, arcades, and gambling industries':0.,
 'Analytical laboratory instrument manufacturing':0.,
 'Animal (except poultry) slaughtering, rendering, and processing':0.,
 'Animal production, except cattle and poultry and eggs':0.,
 'Apparel accessories and other apparel manufacturing':0.,
 'Apparel knitting mills':0.,
 'Apparel, Piece Goods, and Notions Wholesalers':0.,
 'Architectural, engineering, and related services':0.,
 'Arms, ordnance, and accessories manufacturing':0.,
 'Artificial and synthetic fibers and filaments manufacturing':0.,
 'Asphalt paving mixture and block manufacturing':0.,
 'Asphalt shingle and coating materials manufacturing':0.,
 'Audio and video equipment manufacturing':0.,
 'Automatic environmental control manufacturing':0.,
 'Automobile manufacturing':0.,
 'Automotive equipment rental and leasing':0.,
 'Automotive repair and maintenance, except car washes':0.,
 'Ball and roller bearing manufacturing':0.,
 'Bare printed circuit board manufacturing':0.,
 'Bauxite Mining':0.,
 'Beet sugar manufacturing':0.,
 'Biological product (except diagnostic) manufacturing':0.,
 'Biomass Power Generation':0.,
 'Bituminous Coal Underground Mining':0.,
 'Bituminous Coal and Lignite Surface Mining':0.,
 'Blind and shade manufacturing':0.,
 'Boat building':0.,
 'Book publishers':0.,
 'Bowling centers':0.,
 'Bread and bakery product manufacturing':0.,
 'Breakfast cereal manufacturing':0.,
 'Breweries':0.,
 'Brick, tile, and other structural clay product manufacturing':0.,
 'Broadcast and wireless communications equipment':0.,
 'Broadwoven fabric mills':0.,
 'Broom, brush, and mop manufacturing':0.,
 'Building Material and Garden Equipment and Supplies Dealers':0.,
 'Business support services':0.,
 'Cable and other subscription programming':0.,
 'Car washes':0.,
 'Carbon and graphite product manufacturing':0.,
 'Carbon black manufacturing':0.,
 'Carpet and rug mills':0.,
 'Cattle ranching and farming':0.,
 'Cement manufacturing':0.,
 'Cheese manufacturing':0.,
 'Child day care services':0.,
 'Chocolate and confectionery manufacturing from cacao beans':0.,
 'Clay and nonclay refractory manufacturing':0.,
 'Clothing and Clothing Accessories Stores':0.,
 'Coal Power Generation':0.,
 'Coated and laminated paper, packaging paper and plastics film manufacturing':0.,
 'Coating, engraving, heat treating and allied activities':0.,
 'Coffee and tea manufacturing':0.,
 'Commercial and industrial machinery and equipment rental and leasing':0.,
 'Commercial and industrial machinery and equipment repair and maintenance':0.,
 'Communication and energy wire and cable manufacturing':0.,
 'Community food, housing, and other relief services, including rehabilitation services':0.,
 'Computer storage device manufacturing':0.,
 'Computer systems design services':0.,
 'Computer terminals and other computer peripheral equipment manufacturing':0.,
 'Concrete pipe, brick, and block manufacturing':0.,
 'Confectionery manufacturing from purchased chocolate':0.,
 'Construction machinery manufacturing':0.,
 'Cookie, cracker, and pasta manufacturing':0.,
 'Copper Mining':0.,
 'Copper rolling, drawing, extruding and alloying':0.,
 'Cotton farming':0.,
 'Couriers and messengers':0.,
 'Crown and closure manufacturing and metal stamping':0.,
 'Crude Petroleum and Natural Gas Extraction':0.,
 'Curtain and linen mills':0.,
 'Custom architectural woodwork and millwork manufacturing':0.,
 'Custom computer programming services':0.,
 'Cut and sew apparel contractors':0.,
 'Cut stone and stone product manufacturing':0.,
 'Cutlery, utensil, pot, and pan manufacturing':0.,
 'Cutting tool and machine tool accessory manufacturing':0.,
 'Dairy cattle and milk production':0.,
 'Data processing, hosting, and related services':0.,
 'Death care services':0.,
 'Dental equipment and supplies manufacturing':0.,
 'Directory, mailing list, and other publishers':0.,
 'Distilleries':0.,
 'Dog and cat food manufacturing':0.,
 'Doll, toy, and game manufacturing':0.,
 'Drilling oil and gas wells':0.,
 'Dry, condensed, and evaporated dairy product manufacturing':0.,
 'Dry-cleaning and laundry services':0.,
 'Electric Bulk Power Transmission and Control':0.,
 'Electric Power Distribution':0.,
 'Electric lamp bulb and part manufacturing':0.,
 'Electrical and Electronic Goods Wholesalers':0.,
 'Electricity and signal testing instruments manufacturing':0.,
 'Electromedical and electrotherapeutic apparatus manufacturing':0.,
 'Electron tube manufacturing':0.,
 'Electronic and precision equipment repair and maintenance':0.,
 'Electronic capacitor, resistor, coil, transformer, and other inductor manufacturing':0.,
 'Electronic computer manufacturing':0.,
 'Electronic connector manufacturing':0.,
 'Electronics and Appliance Stores':0.,
 'Elementary and secondary schools':0.,
 'Employment services':0.,
 'Engineered wood member and truss manufacturing':0.,
 'Environmental and other technical consulting services':0.,
 'Fabric coating mills':0.,
 'Fabricated pipe and pipe fitting manufacturing':0.,
 'Facilities support services':0.,
 'Farm machinery and equipment manufacturing':0.,
 'Fats and oils refining and blending':0.,
 'Ferrous metal foundries':0.,
 'Fertilizer manufacturing':0.,
 'Fiber, yarn, and thread mills':0.,
 'Fishing':0.,
 'Fitness and recreational sports centers':0.,
 'Flat glass manufacturing':0.,
 'Flavoring syrup and concentrate manufacturing':0.,
 'Flour milling and malt manufacturing':0.,
 'Fluid milk and butter manufacturing':0.,
 'Fluid power process machinery':0.,
 'Food services and drinking places':0.,
 'Food, Beverage, Health, and Personal Care Stores':0.,
 'Footwear manufacturing':0.,
 'Forest nurseries, forest products, and timber tracts':0.,
 'Frozen food manufacturing':0.,
 'Fruit and vegetable canning, pickling, and drying':0.,
 'Fruit farming':0.,
 'Funds, trusts, and other financial vehicles':0.,
 'Furniture and Home Furnishings Stores':0.,
 'Gasket, packing, and sealing device manufacturing':0.,
 'Gasoline Stations':0.,
 'General Merchandise Stores':0.,
 'General and consumer goods rental except video tapes and discs':0.,
 'Geothermal Power Generation':0.,
 'Glass container manufacturing':0.,
 'Glass product manufacturing made of purchased glass':0.,
 'Gold Ore Mining':0.,
 'Grain farming':0.,
 'Grantmaking, giving, and social advocacy organizations':0.,
 'Greenhouse, nursery, and floriculture production':0.,
 'Grocery and Related Product Wholesalers':0.,
 'Ground or treated mineral and earth manufacturing':0.,
 'Guided missile and space vehicle manufacturing':0.,
 'Handtool manufacturing':0.,
 'Hardware manufacturing':0.,
 'Heating equipment (except warm air furnaces) manufacturing':0.,
 'Heavy duty truck manufacturing':0.,
 'Home health care services':0.,
 'Hospitals':0.,
 'Hotels and motels, including casino hotels':0.,
 'Household cooking appliance manufacturing':0.,
 'Household laundry equipment manufacturing':0.,
 'Household refrigerator and home freezer manufacturing':0.,
 'Hydroelectric Power Generation':0.,
 'Ice cream and frozen dessert manufacturing':0.,
 'In-vitro diagnostic substance manufacturing':0.,
 'Independent artists, writers, and performers':0.,
 'Individual and family services':0.,
 'Industrial gas manufacturing':0.,
 'Industrial mold manufacturing':0.,
 'Industrial process furnace and oven manufacturing':0.,
 'Industrial process variable instruments manufacturing':0.,
 'Institutional furniture manufacturing':0.,
 'Insurance agencies, brokerages, and related activities':0.,
 'Insurance carriers':0.,
 'Internet publishing and broadcasting':0.,
 'Internet service providers and web search portals':0.,
 'Investigation and security services':0.,
 'Iron and steel mills and ferroalloy manufacturing':0.,
 'Iron ore mining':0.,
 'Irradiation apparatus manufacturing':0.,
 'Jewelry and silverware manufacturing':0.,
 'Junior colleges, colleges, universities, and professional schools':0.,
 'Knit fabric mills':0.,
 'Laminated plastics plate, sheet (except packaging), and shape manufacturing':0.,
 'Landfill Gas Power Generation':0.,
 'Lawn and garden equipment manufacturing':0.,
 'Lead Ore and Zinc Ore Mining':0.,
 'Leather and hide tanning and finishing':0.,
 'Legal services':0.,
 'Lessors of nonfinancial intangible assets':0.,
 'Light truck and utility vehicle manufacturing':0.,
 'Lighting fixture manufacturing':0.,
 'Lime and gypsum product manufacturing':0.,
 'Logging':0.,
 'Lumber and Other Construction Materials Wholesalers':0.,
 'Magnetic and optical recording media manufacturing':0.,
 'Management of companies and enterprises':0.,
 'Management, scientific, and technical consulting services':0.,
 'Manufactured home (mobile home) manufacturing':0.,
 'Material handling equipment manufacturing':0.,
 'Mattress manufacturing':0.,
 'Mechanical power transmission equipment manufacturing':0.,
 'Medical and diagnostic labs and outpatient and other ambulatory care services':0.,
 'Medicinal and botanical manufacturing':0.,
 "Men's and boys' cut and sew apparel manufacturing":0.,
 'Metal and other household furniture manufacturing':0.,
 'Metal can, box, and other metal container (light gauge) manufacturing':0.,
 'Metal cutting and forming machine tool manufacturing':0.,
 'Metal tank (heavy gauge) manufacturing':0.,
 'Military armored vehicle, tank, and tank component manufacturing':0.,
 'Mineral wool manufacturing':0.,
 'Mining and oil and gas field machinery manufacturing':0.,
 'Miscellaneous Durable Goods Wholesalers':0.,
 'Miscellaneous Nondurable Goods Wholesalers':0.,
 'Miscellaneous Store Retailers':0.,
 'Miscellaneous nonmetallic mineral products':0.,
 'Monetary authorities and depository credit intermediation':0.,
 'Motion picture and video industries':0.,
 'Motor Vehicle and Machinery, Equipment, and Supplies Wholesalers':0.,
 'Motor Vehicle and Parts Dealers':0.,
 'Motor and generator manufacturing':0.,
 'Motor home manufacturing':0.,
 'Motor vehicle body manufacturing':0.,
 'Motor vehicle parts manufacturing':0.,
 'Motorcycle, bicycle, and parts manufacturing':0.,
 'Museums, historical sites, zoos, and parks':0.,
 'Musical instrument manufacturing':0.,
 'Narrow fabric mills and schiffli machine embroidery':0.,
 'Natural Gas Liquid Extraction':0.,
 'Natural Gas Power Generation':0.,
 'Natural gas distribution':0.,
 'Newspaper publishers':0.,
 'Nickel Mining':0.,
 'Nonchocolate confectionery manufacturing':0.,
 'Nondepository credit intermediation and related activities':0.,
 'Nonferrous metal (except copper and aluminum) rolling, drawing, extruding and alloying':0.,
 'Nonferrous metal foundries':0.,
 'Nonresidential commercial and health care structures':0.,
 'Nonresidential maintenance and repair':0.,
 'Nonresidential manufacturing structures':0.,
 'Nonstore Retailers':0.,
 'Nonupholstered wood household furniture manufacturing':0.,
 'Nonwoven fabric mills':0.,
 'Nuclear Electric Power Generation':0.,
 'Nursing and residential care facilities':0.,
 'Office administrative services':0.,
 'Office furniture manufacturing':0.,
 'Office supplies (except paper) manufacturing':0.,
 'Offices of physicians, dentists, and other health practitioners':0.,
 'Oilseed farming':0.,
 'Ophthalmic goods manufacturing':0.,
 'Optical instrument and lens manufacturing':0.,
 'Ornamental and architectural metal products manufacturing':0.,
 'Other Electric Power Generation':0.,
 'Other Metal Ore Mining':0.,
 'Other accommodations':0.,
 'Other aircraft parts and auxiliary equipment manufacturing':0.,
 'Other amusement and recreation industries':0.,
 'Other animal food manufacturing':0.,
 'Other basic organic chemical manufacturing':0.,
 'Other commercial and service industry machinery manufacturing':0.,
 'Other communications equipment manufacturing':0.,
 'Other computer related services, including facilities management':0.,
 'Other concrete product manufacturing':0.,
 'Other cut and sew apparel manufacturing':0.,
 'Other educational services':0.,
 'Other electronic component manufacturing':0.,
 'Other engine equipment manufacturing':0.,
 'Other fabricated metal manufacturing':0.,
 'Other general purpose machinery manufacturing':0.,
 'Other industrial machinery manufacturing':0.,
 'Other information services':0.,
 'Other leather and allied product manufacturing':0.,
 'Other major household appliance manufacturing':0.,
 'Other nonmetallic mineral mining and quarrying':0.,
 'Other nonresidential structures':0.,
 'Other personal services':0.,
 'Other plastics product manufacturing':0.,
 'Other pressed and blown glass and glassware manufacturing':0.,
 'Other residential structures':0.,
 'Other rubber product manufacturing':0.,
 'Other support services':0.,
 'Packaging machinery manufacturing':0.,
 'Paint and coating manufacturing':0.,
 'Paper mills':0.,
 'Paperboard Mills':0.,
 'Paperboard container manufacturing':0.,
 'Performing arts companies':0.,
 'Periodical publishers':0.,
 'Personal and household goods repair and maintenance':0.,
 'Personal care services':0.,
 'Pesticide and other agricultural chemical manufacturing':0.,
 'Petrochemical manufacturing':0.,
 'Petroleum Power Generation':0.,
 'Petroleum lubricating oil and grease manufacturing':0.,
 'Petroleum refineries':0.,
 'Petroleum, Chemical, and Allied Products Wholesalers':0.,
 'Pharmaceutical preparation manufacturing':0.,
 'Photographic and photocopying equipment manufacturing':0.,
 'Photographic services':0.,
 'Pipeline transportation':0.,
 'Plastics and rubber industry machinery manufacturing':0.,
 'Plastics bottle manufacturing':0.,
 'Plastics material and resin manufacturing':0.,
 'Plastics packaging materials and unlaminated film and sheet manufacturing':0.,
 'Plastics pipe and pipe fitting manufacturing':0.,
 'Plate work and fabricated structural product manufacturing':0.,
 'Plumbing fixture fitting and trim manufacturing':0.,
 'Polystyrene foam product manufacturing':0.,
 'Postal service':0.,
 'Pottery, ceramics, and plumbing fixture manufacturing':0.,
 'Poultry and egg production':0.,
 'Poultry processing':0.,
 'Power boiler and heat exchanger manufacturing':0.,
 'Power, distribution, and specialty transformer manufacturing':0.,
 'Power-driven handtool manufacturing':0.,
 'Prefabricated wood building manufacturing':0.,
 'Primary battery manufacturing':0.,
 'Primary smelting and refining of copper':0.,
 'Primary smelting and refining of nonferrous metal (except copper and aluminum)':0.,
 'Printed circuit assembly (electronic assembly) manufacturing':0.,
 'Printing':0.,
 'Printing ink manufacturing':0.,
 'Promoters of performing arts and sports and agents for public figures':0.,
 'Propulsion units and parts for space vehicles and guided missiles':0.,
 'Pulp mills':0.,
 'Pump and pumping equipment manufacturing':0.,
 'Radio and television broadcasting':0.,
 'Rail transportation (Diesel)':0.,
 'Rail transportation (Electric)':0.,
 'Railroad rolling stock manufacturing':0.,
 'Ready-mix concrete manufacturing':0.,
 'Real estate':0.,
 'Reconstituted wood product manufacturing':0.,
 'Relay and industrial control manufacturing':0.,
 'Residential maintenance and repair':0.,
 'Residential permanent site single- and multi-family structures':0.,
 'Rolling mill and other metalworking machinery manufacturing':0.,
 'Rubber and plastics hoses and belting manufacturing':0.,
 'Sand, gravel, clay, and ceramic and refractory minerals mining and quarrying':0.,
 'Sanitary paper product manufacturing':0.,
 'Sawmills and wood preservation':0.,
 'Scientific research and development services':0.,
 'Seafood product preparation and packaging':0.,
 'Search, detection, and navigation instruments manufacturing':0.,
 'Seasoning and dressing manufacturing':0.,
 'Secondary smelting and alloying of aluminum':0.,
 'Securities, commodity contracts, investments, and related activities':0.,
 'Semiconductor and related device manufacturing':0.,
 'Semiconductor machinery manufacturing':0.,
 'Services to buildings and dwellings':0.,
 'Ship building and repairing':0.,
 'Showcase, partition, shelving, and locker manufacturing':0.,
 'Sign manufacturing':0.,
 'Small electrical appliance manufacturing':0.,
 'Snack food manufacturing':0.,
 'Soap and cleaning compound manufacturing':0.,
 'Soft drink and ice manufacturing':0.,
 'Software publishers':0.,
 'Software, audio, and video media reproducing':0.,
 'Solar Power Generation':0.,
 'Sound recording industries':0.,
 'Soybean and other oilseed processing':0.,
 'Special tool, die, jig, and fixture manufacturing':0.,
 'Specialized design services':0.,
 'Spectator sports':0.,
 'Speed changer, industrial high-speed drive, and gear manufacturing':0.,
 'Sporting and athletic goods manufacturing':0.,
 'Spring and wire product manufacturing':0.,
 'Stationery product manufacturing':0.,
 'Steel product manufacturing from purchased steel':0.,
 'Stone mining and quarrying':0.,
 'Storage battery manufacturing':0.,
 'Sugar cane mills and refining':0.,
 'Sugarcane and sugar beet farming':0.,
 'Support activities for agriculture and forestry':0.,
 'Support activities for oil and gas operations':0.,
 'Support activities for other mining':0.,
 'Support activities for printing':0.,
 'Support activities for transportation':0.,
 'Surgical and medical instrument manufacturing':0.,
 'Surgical appliance and supplies manufacturing':0.,
 'Switchgear and switchboard apparatus manufacturing':0.,
 'Synthetic dye and pigment manufacturing':0.,
 'Synthetic rubber manufacturing':0.,
 'Tar Sands Extraction':0.,
 'Telecommunications':0.,
 'Telephone apparatus manufacturing':0.,
 'Textile and fabric finishing mills':0.,
 'Textile bag and canvas mills':0.,
 'Tire manufacturing':0.,
 'Tobacco product manufacturing':0.,
 'Toilet preparation manufacturing':0.,
 'Totalizing fluid meters and counting devices manufacturing':0.,
 'Transit and ground passenger transportation':0.,
 'Travel arrangement and reservation services':0.,
 'Travel trailer and camper manufacturing':0.,
 'Tree nut farming':0.,
 'Truck trailer manufacturing':0.,
 'Truck transportation':0.,
 'Turbine and turbine generator set units manufacturing':0.,
 'Turned product and screw, nut, and bolt manufacturing':0.,
 'Unlaminated plastics profile shape manufacturing':0.,
 'Upholstered household furniture manufacturing':0.,
 'Uranium-Radium-Vanadium Ore Mining':0.,
 'Urethane and other foam product (except polystyrene) manufacturing':0.,
 'Valve and fittings other than plumbing':0.,
 'Vegetable and melon farming':0.,
 'Vending, commercial, industrial, and office machinery manufacturing':0.,
 'Veneer and plywood manufacturing':0.,
 'Veterinary services':0.,
 'Warehousing and storage':0.,
 'Waste management and remediation services':0.,
 'Watch, clock, and other measuring and controlling device manufacturing':0.,
 'Water transportation':0.,
 'Water, sewage and other systems':0.,
 'Wave & Tidal Power Generation':0.,
 'Wet corn milling':0.,
 'Wind Power Generation':0.,
 'Wineries':0.,
 'Wiring device manufacturing':0.,
 "Women's and girls' cut and sew apparel manufacturing":0.,
 'Wood container and pallet manufacturing':0.,
 'Wood kitchen cabinet and countertop manufacturing':0.,
 'Wood windows and doors and millwork':0.})
if secrev1 != "":
    X[secrev1] = secrev_pc1/100
if secrev2 != "":
    X[secrev2] = secrev_pc2/100
if secrev3 != "":
    X[secrev3] = secrev_pc3/100
# st.write("The input looks like this", X)
# st.write(X.shape)
# st.write("Working the model with Nadir :) - TBC")
# c_score = 70
# if 'c_score' not in st.session_state:
#     st.session_state['c_score'] = c_score
# st.write("C score placeholder:", st.session_state.c_score)
for key in st.session_state.keys():
        del st.session_state[key]
for i in range(2):
    st.text("")
st.markdown("***")
@st.cache
def load_knn():
    model = joblib.load(os.path.abspath("model/kmeans.pkl"))
    return model
@st.cache
def load_knn_tx():
    tx = joblib.load(os.path.abspath("model/col_transf.pkl"))
    return tx
@st.cache
def load_knn_pca():
    pca = joblib.load(os.path.abspath("model/pca.pkl"))
    return pca
if st.button('Calculate!'):
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.025)
        my_bar.progress(percent_complete + 1)
    for i in range(3):
        st.text("")
    tx = load_knn_tx()
    X_tx = tx.transform(X)
    pca = load_knn_pca()
    X_pca = pca.transform(X_tx)
    model = load_knn()
    result = model.predict(X_pca)
    df = joblib.load(os.path.abspath("model/climate_score_stats_per_cluster.pkl"))
    c_score = "{:.0f}".format(float(df.loc[result,('Climate Score', 'mean')]))

    st.session_state['c_score'] = c_score
    for i in range(3):
        st.text("")
    col1,col1img,space = st.columns([7,1,2])
    with col1:
        word = "<h2>Estimated climate strategy score for your company is...</h2>"
        st.write(word, unsafe_allow_html=True)
        score = f"<h1 class = 'score_cls'>{st.session_state.c_score}</h1>"
        st.write(score, unsafe_allow_html=True)
    with col1img:
        rate_img = Image.open(os.path.abspath("images/rating.png"))
        st.image(rate_img, width=178)

    st.session_state['sector'] = sector
    st.session_state['revenue'] = revenue
    st.session_state['employees'] = employees
    st.session_state['secrev1'] = secrev1
    st.session_state['secrev2'] = secrev2
    st.session_state['secrev3'] = secrev3
    st.session_state['secrev_pc1'] = secrev_pc1
    st.session_state['secrev_pc2'] = secrev_pc2

    st.markdown("***")
    st.write("<h3 class='benmk'>Benchmarking: Comparing with the database</h3>", unsafe_allow_html=True)
    tst = joblib.load(os.path.abspath("model/benchmk_scr.pkl"))
    tst = tst[["Percentile", "Climate Strategy Score", "Selected Company Name"]]
    tst = tst.append({"Climate Strategy Score":float(c_score), "Selected Company Name":"---Our Company---"}, ignore_index=True).sort_values(by="Climate Strategy Score")
    tst.fillna(15., inplace=True)
    tst = tst.style.format({"Percentile":'{:.0f}',"Climate Strategy Score":'{:.0f}'}).hide()
    st.table(tst)
