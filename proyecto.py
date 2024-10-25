import streamlit as st
from streamlit_agraph import agraph,Node,Edge,Config
from PIL import Image
import folium
from folium import plugins

# Configurar la página principal

st.set_page_config(page_title="Interfaz CREmx", page_icon=":school:", layout="wide")

# Agregar estilos CSS personalizados
st.markdown(
    """
    <style>
    .horizontal-menu {
        display: flex;
        justify-content: center;
        background-color: #FFD700;
        padding: 10px 0;
        font-size: 18px;
    }
    .horizontal-menu button {
        background-color: #FFA500;
        border: none;
        padding: 10px 20px;
        color: white;
        font-weight: bold;
        cursor: pointer;
        margin: 0 10px;
        border-radius: 10px;
    }
    .horizontal-menu button:hover {
        background-color: #FF8C00;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Inicializar el estado de la opción seleccionada si no existe
if 'selected_option' not in st.session_state:
    st.session_state['selected_option'] = "Inicio"

# Crear un menú de navegación horizontal usando botones y CSS
st.markdown('<div class="horizontal-menu">', unsafe_allow_html=True)

# Crear los botones de navegación
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col1:
    if st.button("INICIO"):
        st.session_state['selected_option'] = "Inicio"
with col2:
    if st.button("IMPACTO CREmx"):
        st.session_state['selected_option'] = "Impacto CREmx"
with col3:
    if st.button("MÉXICO Y SU EDUCACIÓN"):
        st.session_state['selected_option'] = "México y su Educación"
with col4:
    if st.button("INFORME ANUAL"):
        st.session_state['selected_option'] = "Informe Anual"
with col5:
    if st.button("CONTACTO"):
        st.session_state['selected_option'] = "Contacto"
with col6:
    if st.button("CURSOS Y TALLERES"):
        st.session_state['selected_option'] = "Cursos y talleres"
with col7:
    if st.button("HERRAMIENTAS DE DIAGNÓSTICO"):
        st.session_state['selected_option'] = "Herramientas"

st.markdown('</div>', unsafe_allow_html=True)

# Contenido de cada sección
if st.session_state['selected_option'] == "Inicio":
    st.title("Bienvenido a CREmx")
    st.markdown("### Programa que refuerza el desarrollo socioemocional y educativo")
    st.video("Sueños Cremx.mp4")
    st.write("Compromiso y responsabilidad educativa, A.B.P es una asociación sin fines de lucro dedicada a la mejora educativa en México")
    with st.expander("Mision"):
        st.write('''Brindar herramientas formativas de desarrollo con principios humanísticos a niños, niñas y jóvenes en condiciones de vulnerabilidad
        con la participación de actores claves de la educación para ejercer su derecho a una educación de calidad ''')
        st.image("Misionimage.png")
    with st.expander("Vision"):
        st.write(''' Ser una institución líder en México que apoya una educación preventiva, formativa, humanística y de calidad que contribuya
                al desarrollo social''')
        st.image("Visionimage.png")
    with st.expander("Historia"):
        st.write('''La historia de la organización, el fundador, quién es y como surgio la idea de fundar la organización ''')
        
    colum1, colum2, colum3= st.columns(3, vertical_alignment="bottom")
    with colum1:
        st.image("Proyectovidaimage.png", use_column_width="auto")
        st.subheader('''Programa de educación sociemocional "Proyecto de vida" ''')
        st.write("Se implementa en las escuelas públicas de México")
        with st.expander("Ver más"):
            html_code = """<iframe src="https://cremx.org/proyectodevida/" width="always" height="400"></iframe>"""
            st.components.v1.html(html_code, height=400)
    with colum2:
        st.image("Vanguardiaimage.png", use_column_width="auto")
        st.subheader("Revista Vanguardia Educativa")
        st.write("Revista de edición trimestral con temas de actualidad en educación")
        with st.expander("Ver más"):
            html_code = """<iframe src="https://cremx.org/revistavanguardiaeducativa/" width="always" height="400"></iframe>"""
            st.components.v1.html(html_code, height=400)
            
    with colum3:
        st.image("Congreso.png", use_column_width="auto")
        st.subheader("Congreso Mundial de Educación")
        st.write("Foro anual de grandes líderes de la educación")
        with st.expander("Ver Más"):
            html_code = """<iframe src="https://cremx.org/congresomundialdeeducacion/" width="always" height="400"></iframe>"""
            st.components.v1.html(html_code, height=400)
            
    with st.container(border=True):
        
        ccolum1,ccolum2=st.columns(2,)
        with ccolum1:
            with st.container():
                st.header("Contacto")
                st.subheader("Oficinas")
                st.write("Dirección: Vía Julio Cesar 615 \n\nFuentes del Valle, 66220 San Pedro\nGarza García, N.L\n\nTeléfono: (81) 8378 5007\n\nCorreo:proyectos@cremx.org")
                map_center=[25.66300731045276, -100.35628136471323]
                m=folium.Map(location=map_center,zoom_start=30)
                folium.Marker(location=[25.66300731045276, -100.35628136471323],popup="Nuestras oficinas").add_to(m)
                st.components.v1.html(m._repr_html_(), height=500)
        with ccolum2:
            with st.container():
                name=st.text_input("Nombre completo")
                email=st.text_input("Correo electrónico")
                cel=st.text_input("Teléfono")
                st.write("\n\n")
                option=st.selectbox("¿Cómo te enteraste de nosotros", ("Revista Vanguardia Educativa","Congreso Mundial de Educación","Escuelas","Redes sociales","Otro"))
                text=st.text_area("Mensaje")
                st.button("Enviar")
    
    
elif st.session_state['selected_option'] == "Impacto CREmx":
    with st.container():
        st.image("CREmxBanner.png", use_column_width="always")
        video,texto,logo=st.columns(3)
        with video:
            st.video("Testimoniales CRE.mp4")
        with texto:
            st.markdown('''Programa que refuerza el desarrollo socioemocinal a estudiantes de escuelas en zonas vulnerables y que disminuye los factores
                            de riesgo que derivan en deserción escolar. Esto se logra mediante 4 programas que CREmx ha diseñado e implementado para cubrir
                            las 5 dimensiones que conforman la educación socioemocional, programa que está alineado a todos los objetivos de la SEP. Como
                            parte de nuestra estrategia, involucramos a padres de familia, maestros y directivos para coordinar los esfuerzos de escuela-familia,
                            en beneficio de los niños(as) y adolescentes''')
        with logo:
            st.image("Pvida.png")
        logo2,texto2,video2=st.columns(3)
        with logo2:
            st.image("Vanedu.png")
        with texto2:
            st.markdown('''Revista publicada de manera trimestral dirigida a maestros, docentes, y directivos de instituciones educativas con el fin de compartir
                        temas de actualidad relacionados con la educación en sus distintos enfoques (neurológico, pedagógico, humanístico,etc). Su objetivo es
                        hacer llegar a los magistrados información bien fundamentada que los oriente en su labor en las aulas con los temás de interés a nivel internacional''')
        with video2:
            st.video("Revista Vanguardia Educativa.mp4")
            
        video3,texto3,logo3=st.columns(3)
        with video3:
            st.video("Los regios están despiertos.mp4")
        with texto3:
            st.markdown('''Congreso organizado anualmente en el cual se invitan a ponentes y líderes en educación de talla internacional. Al igual que la revista este congreso está
                        dirigido a todo involucrado en docencia en donde se tiene la oportunidad de convivir con iguales en profesión e intereses. \nEste congreso tiene como objetivo
                        traer a nuestro país expertos que nos compartan temas de vanguardia educativa''')
        with logo3:
            st.image("Congr.png")
    st.write("Con estas tres iniciativas CREmx ha beneficiado  más de 150,000 estudiantes, maestros y padres de familia. \nLa educación de calidad es un derecho de todos... !para bien de todos¡")

elif st.session_state['selected_option'] == "México y su Educación":
    with st.container():
        st.image("MexEduBanner.png", use_column_width="always")
        text, image=st.columns(2)
        with text:
            st.markdown('''México tiene entre 200,000 y 500,000 mentes brillantes y sólo 14,000-20,000 son de nivel socio económico A/B ¡480,000 mexicanos talentosos se pierden por falta de oportunidades!...
                        \n\nAntonio Cruz en CNN&mdash; Junio 2013''')
            st.markdown('''En México informes oficiales del gobierno señalan que la deserción escolar afecta a una cuarta parte de la población estudiantil, con una diferencia por nivel socioeconómico
                        de 21% en sectores ricos y 27% en la población más pobre. Sin embargo estas cifras extraoficiales señalan más del 40% de deserción en algunas zonas vulnerables.''')
            st.markdown('''Debido al actual confinamiento por covid 19 estas cifras se verán drasticamente incrementadas''')
        with image:
            st.image("niñosedu.png",use_column_width="always")
        image2,text2=st.columns(2)
        with image2:
            st.image("niñoed.png",use_column_width="always")
        with text2:
            st.markdown('''El Banco Mundial y la OCDE en 2016 señalaron que en México 7.5 millones de jóvenes ni estudian ni trabajan (los llamados Ninis), algunos laboran en el comercio informal,
                        otros se adhieren a organizaciones delictivas.\n\nLa Junta Intersercretarial del Gobierno Estatal de Nuevo León reveló que cerca de 55,000 menores abandonaron la escuela en ciclo
                        escolar 2016-2017, casi el doble de los 28,000 que dejaron la escuela en el periodo 2014-2015, mencionando que los principales motivos de esta deserción escolar son: ''')
            st.markdown(''':round_pushpin: Bajas expectativas profesionales de los padres, del entorno y del alumno sobre si mismo.\n\n:round_pushpin: Influencias perjudiciales del ambiente (pandillerismo,drogadicción).\n\n:round_pushpin: Rezago educativo y socioemocional\n\n:round_pushpin: El dinero fácil por la vía ilegal.\n\n:round_pushpin: Necesidad de trabajar para solventar las necesidades de su hogar.''')
            st.markdown('''En Compromiso y Responsabilidad Educativa A.B.P trabajamos con niños y jóvenes reduciendo los factores de riesgo que derivan en deserción escolar, preveniendo que recurran a la
                        delicuencia como una forma de solventar sus necesidades y formando seres humanos comprometidos y capaces de enfrentar los retos de su entorno''')
elif st.session_state['selected_option'] == "Informe Anual":
   with st.container():
       if 'selected_option' not in st.session_state:
           st.session_state['selected_option'] = "2019"
       st.markdown('<div class="horizontal-menu">', unsafe_allow_html=True)
       asub,sub,sub1, sub2, sub3, sub4, sub5,sub6,sub7 = st.columns(9)
       with sub1:
           if st.button("2019"):
               st.session_state['selected_option']="2019"
       with sub2:
           if st.button("2020"):
               st.session_state['selected_option']="2020"
       with sub3:
           if st.button("2021"):
               st.session_state['selected_option']="2021"
       with sub4:
           if st.button("2022"):
               st.session_state['selected_option']="2022"
       with sub5:
           if st.button("2023"):
               st.session_state['selected_option']="2023"
   if st.session_state['selected_option']=="2019":
       st.header("Índice")
       c1,c2,c3=st.columns(3)
       with c2:
           st.markdown('''I. Mensaje de la directora\n\nII. ¿Quienes somos?\n\nIII. Misión y Visión\n\nIV. Objetivo general y visión de cambio\n\nV.Ejes de intervención CREmx\n\nVI. Informe financiero\n\nVII. Agradecimientos a nuestros aliados''')
           
       with st.container():
           st.header("I. Mensaje de la directora")
           st.markdown('''En palabras del filósofo griego Heráclito:
la única constante es el cambio. El 2020
marcó un punto de inflexión en la sociedad a nivel mundial, ha sido la etapa de la
humanidad con mayor cambio que
hemos vivido, puso a prueba nuestras habilidades adaptativas como seres humanos, como familia y como sociedad.''')
           st.markdown('''Tiempos difíciles forman seres humanos fuertes. La pandemia nos obligó a pausar nuestras vidas y reflexionar sobre los aspectos más sensibles y más humanos: nos hizo darnos cuenta del valor de nuestro tiempo y la importancia de dedicárselo a nuestros seres queridos mientras estén con nosotros, nos hizo ver la importancia de la naturaleza en el futuro de la
                    humanidad y de la especie; nos hizo descubrir de que tenemos una gran capacidad para cambiar nuestros hábitos y modo de vida para mejorar como individuos y como sociedad.
                    El equipo de CREmx, en estos tiempos difíciles, superó cada gran reto que se le presentaba, y en este camino hemos hecho excelentes amigos que ahora son nuestros aliados. Pero más allá de las dificultades técnicas salvadas, tuvimos la oportunidad de ver claramente aspectos clave del desarrollo del niño que quedaron evidenciados con estas circustancias de vida tan dramáticas. Y actuando con presteza y acertadamente repensamos nuestros
                    programas para dar más importancia a la educación socioemocional y a los aprendizajes basales en la educación de los niños, sin los cuales no podría siquiera aspirar a una educación''')
           st.header("II.¿Quiénes somos CREmx?")
           st.markdown('''Compromiso y Responsabilidad Educativa es una asociación de beneficencia privada que tiene
como objetivo disminuir los factores de riesgo que deriven en la deserción escolar, mediante
distintos programas focalizados estratégicamente a mitigar diversos riesgos, apoyando así una
educación de calidad y logrando con ello el fortalecimiento del tejido social. El Programa Proyecto de Vida, la Revista Vanguardia Educativa y el Congreso Mundial de Educación. Estas tres líneas de intervención generan en docentes y personal educativo la
                capacidad de brindar una educación de calidad a niños y adolescentes, permitiéndoles adaptarse al cambio tan acelerado que hay en la realidad educativa y social. Nuestro trabajo se dirige bajo el principio de que sólo a través de la educación podemos dirigir de manera sistémica el rumbo de nuestra vida, nuestra familia, nuestra sociedad y nuestro país.
                Está inmerso en nuestra naturaleza de seres humanos crecer en grupo, en comunidad. Es a través del encuentro con el otro que crecemos, que nos hacemos mejores personas y es gracias a esa naturaleza social que podemos mostrar la mejor versión de nosotros mismos en nuestras relaciones interpersonales. ''')
           st.image("Seccioninforme.png")
           st.header("III. Misión y Visión")
           with st.expander("Mision"):
               st.write('''Brindar herramientas formativas de desarrollo con principios humanísticos a niños, niñas y jóvenes en condiciones de vulnerabilidad con la participación de actores claves de la educación para ejercer su derecho a una educación de calidad ''')
           with st.expander("Vision"):
               st.write(''' Ser una institución líder en México que apoya una educación preventiva, formativa, humanística y de calidad que contribuya al desarrollo social''')
               
           st.title("VII. Agradecimiento a nuestros aliados")
           organizacion=Node(id="Organizacion",label="CREmx",size=40,image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfI8vG6dBpG3cSYX5vnU2JA3ssK_zez2lbnw&s",shape="circularImage")
           aliado1=Node(id="aeromexico",label="AeroMéxico",size=25,image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTONSbYr6BG04zowEagQzS6eFvH6dFhrv-lag&s",shape="circularImage")
           aliado2=Node(id="allen",label="Grupo Allen",size=25,image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTv8SFGys-1zJihRR-Nu8ru4gjefGBqSoi3KQ&s",shape="circularImage")
           aliado3=Node(id="arca",label="Embotelladoras Arca",size=25,image="https://cdn.worldvectorlogo.com/logos/embotelladoras-arca.svg",shape="circularImage")
           aliado4=Node(id="asociacionhoteles",label="Asociación Mexicana de Hoteles de Nuevo León,A.C",size=25,image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGz0bPWUhoma0smxGTSIXbfmW0X2y1YhusvQ&s",shape="circularImage")
           aliado5=Node(id="bien",label="Bien",size=25,image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSok6bqEeeT_ylqmvvfkFktDm1MXmbYz_6E1A&s",shape="circularImage")
           aliado6=Node(id="caaarem",label="Fundación Caaarem",size=25,image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjJLCouZY4HFiJBwIKDXpulPnZscZiw8bllA&s",shape="circularImage")
           aliado7=Node(id="carmona",label="Carmona Impresores",size=25,image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8sf8QD3Iec1vHcadRi-kUUR93RJuVPQeKgA&s",shape="circularImage")
           aliado8=Node(id="cemex",label="CEMEX",size=25,image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHz4_omSNtkdvbI3zUxUVMYVi6cr6L6QboKA&s",shape="circularImage")
           aliado9=Node(id="cemix",label="Fundación Cemix",size=25,image="https://www.cemix.com/wp-content/uploads/2020/09/Fundacion-Logo.jpg",shape="circularImage")
           aliado10=Node(id="clix",label="CLIX",size=25,image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJ6oLpsXRVNd_A1MyCtQ1InkxMy4N3rzsDBg&s",shape="circularImage")
           arista1= Edge(source="Organizacion",target="aeromexico")
           arista2= Edge(source="Organizacion",target="allen")
           arista3= Edge(source="Organizacion",target="arca")
           arista4= Edge(source="Organizacion",target="asociacionhoteles")
           arista5= Edge(source="Organizacion",target="bien")
           arista6= Edge(source="Organizacion",target="caaarem")
           arista7= Edge(source="Organizacion",target="carmona")
           arista8= Edge(source="Organizacion",target="cemex")
           arista9= Edge(source="Organizacion",target="cemix")
           arista10= Edge(source="Organizacion",target="clix")
           config = Config(width=800, 
                height=600, 
                directed=False,  # No se necesita que las aristas sean direccionales
                nodeHighlightBehavior=True, 
                highlightColor="#F7A7A6", 
                collapsible=False)
           agraph(nodes=[organizacion,aliado1,aliado2,aliado3,aliado4,aliado5,aliado6,aliado7,aliado8,aliado9,aliado10],edges=[arista1,arista2,arista3,arista4,arista5,arista6,arista7,arista8,arista9,arista10],config=config)

           
elif st.session_state['selected_option'] == "Contacto":
    clm1,clm2=st.columns(2)
    with clm1:
        with st.container():
            st.header("Contacto")
            st.subheader("Oficinas")
            st.write("Dirección: Vía Julio Cesar 615 \n\nFuentes del Valle, 66220 San Pedro\nGarza García, N.L\n\nTeléfono: (81) 8378 5007\n\nCorreo:proyectos@cremx.org")
            map_center=[25.66300731045276, -100.35628136471323]
            m=folium.Map(location=map_center,zoom_start=30)
            folium.Marker(location=[25.66300731045276, -100.35628136471323],popup="Nuestras oficinas").add_to(m)
            st.components.v1.html(m._repr_html_(), height=500)
    with clm2:
        with st.container():
            name=st.text_input("Nombre completo")
            email=st.text_input("Correo electrónico")
            cel=st.text_input("Teléfono")
            st.write("\n\n")
            option=st.selectbox("¿Cómo te enteraste de nosotros?", ("Revista Vanguardia Educativa","Congreso Mundial de Educación","Escuelas","Redes sociales","Otro"))
            text=st.text_area("Mensaje")
            st.button("Enviar")

elif st.session_state['selected_option'] == "Cursos y talleres":
    with st.container():
        curso1,curso2,curso3=st.columns(3,gap="medium")
        with curso1:
            st.image("curso1.jpg",width=200)
            st.subheader("LectoEscritura")
            with st.expander("Ver material"):
                v1,v2,v3=st.columns(3)
                with v1:
                    st.video("Principios del aprendizaje lecto-escritor.mp4")
                    st.caption("Principios del aprendizaje lecto-escritor")
                with v2:
                    st.video("Habilidades necesarias antes de leer y escribir.mp4")
                    st.caption("Habilidades necesarias antes de leer y escribir")
                with v3:
                    st.video("Centros de apoyo lectoescritor gratuitos en México.mp4")
                    st.caption("Centros de apoyo lectoescritor gratuitos en México")
                v4,v5,v6=st.columns(3)
                with v4:
                    st.video("Dislexia y Disgrafia; Trastornos que complican el proceso lectoescritor.mp4")
                    st.caption("Dislexia y Disgrafia: Trastornos que complican el proceso lectoescritor")
                with v5:
                    st.video("Dislexia y Disgrafía; Intervenciones educativas.mp4")
                    st.caption("Dislexia y Disgrafía; Intervenciones educativas")
        with curso2:
            st.image("juegosmesa.png",width=200)
            st.subheader("Juegos de mesa y Neurodesarrollo")
            with st.expander("Ver material"):
                m1,m2,m3=st.columns(3)
                with m1:
                    st.video("Juegos de mesa y neurodesarrollo Parte 1.mp4")
                    st.caption("Juegos de mesa y neurodesarrollo")
                with m2:
                    st.video("Dix it - Empatia y Pensamiento Critico.mp4")
                    st.caption("Dix it -Empatia y Pensamiento Critico")
                with m3:
                    st.video("Catan - Planeación, toma de decisiones y negociación.mp4")
                    st.caption("Catan - Planeación, toma de decisiones y negociación")
                m4,m5,m6=st.columns(3)
                with m4:
                    st.video("Dix it - Storytelling y habilidades comunicativas.mp4")
                    st.caption("Dix it - Storytelling y habilidades comunicativas")
                with m5:
                    st.video("Dix It - Inteligencia y exploración emocional.mp4")
                    st.caption("Dix It - Inteligencia y exploración emocional")
                with m6:
                    st.video("QWIRKLE - Percepción visual y solución de problemas.mp4")
                    st.caption("QWIRKLE - Percepción visual y solución de problemas")
                m7,m8,m9=st.columns(3)
                with m7:
                    st.video("Hedbanz - pensamiento deductivo, inferencial e imaginativo.mp4")
                    st.caption("Hedbanz - Pensamiento deductivo, Inferencial e Imaginativo")
                with m8:
                    st.video("Juegos de mesa y neurodesarrollo parte 2.mp4")
                    st.caption("Juegos de mesa y neurodesarrollo Parte 2")
                with m9:
                    st.video("Juegos de mesa y Neurodesarrollo Parte 3.mp4")
                    st.caption("Juegos de mesa y neurodesarrollo Parte 3")
        with curso3:
            st.image("sueño.jpg",width=200)
            st.subheader("El sueño y el aprendizaje")
            with st.expander("Ver material"):
                s1,s2,s3=st.columns(3)
                with s1:
                    st.video("El sueño y el aprendizaje express.mp4")
                    st.caption("El sueño y el aprendizaje express")
                with s2:
                    st.video("El sueño y el neurodesarrollo Primera Infancia.mp4")
                    st.caption("El sueño y el neurodesarrollo en la Primera Infancia")
        #O usando HTML
        st.subheader("Juegos ludicos para realizar con los niños")
        html_code = """<iframe src="https://www.funbrain.com/" width="800" height="600"></iframe>"""
        st.components.v1.html(html_code, height=600)
        
        
elif st.session_state['selected_option'] == "Herramientas":
    with st.container():
        h1,h2=st.columns(2)
        with h1:
            video_url="https://youtu.be/uPEGVIESwcU?si=CAkQBWJp14wujz3_"
            st.video(video_url)
        with h2:
            st.markdown('''La concientización, diagnóstico y recursos para neurodivergentes son esenciales para promover la inclusión y el bienestar. La concientización ayuda a desestigmatizar condiciones como el autismo y el TDAH, mientras que un diagnóstico temprano permite intervenciones efectivas. Proveer recursos como programas de apoyo y adaptaciones en entornos educativos y laborales mejora la calidad de vida de las personas neurodivergentes y enriquece a la sociedad, fomentando un entorno más diverso y empático.''')
            st.markdown('''Aqui hay algunos de los tipos de neurodivergencia: ''')
            st.markdown(''':round_pushpin: Trastorno del Espectro Autista (TEA)\n\n:round_pushpin: Trastorno por Déficit de Atención e Hiperactividad (TDAH)\n\n:round_pushpin: Dislexia\n\n:round_pushpin: Discalculia\n\n:round_pushpin: Trastorno de la Coordinación del Desarrollo (TDC)''')
        h3,h4,h5=st.columns(3)
        with h3:
            with st.expander("Trastorno por Déficit de Atención e Hiperactividad"):
                videoTDAH="https://www.youtube.com/watch?v=nMJiS3hLg_A"
                st.video(videoTDAH)
                st.markdown('''Se caracteriza por dificultades en la atención, impulsividad y, en algunos casos, hiperactividad. Las personas con TDAH pueden tener problemas para concentrarse y organizar tareas.''')
                st.markdown('''[Escala de Conner](https://www.adhdme.care/indicator-caars)''')
        with h4:
            with st.expander("Trastorno del Espectro Autista"):
                videoTEA="https://www.youtube.com/watch?v=XhmvcCbd6mI"
                st.video(videoTEA)
                st.markdown('''Incluye una variedad de condiciones que afectan la comunicación, la interacción social y el comportamiento. Las personas con TEA pueden tener intereses intensos en temas específicos y presentar una gama de habilidades.''')
                st.markdown('''[Test AQ](https://espectroautista.info/AQ-es.html)''')
        with h5:
            with st.expander("Dislexia"):
                videoDis="https://www.youtube.com/watch?v=bNjr9Y1k0SI"
                st.video(videoDis)
                st.markdown('''Un trastorno del aprendizaje que afecta la habilidad para leer, escribir y, en algunos casos, hablar. Las personas con dislexia pueden tener dificultades para reconocer palabras y comprender textos.''')
                st.markdown('''[Test Dislexia](https://www.testdyslexia.com/)''')
        st.subheader("Instituciones que trabajan con neurodivergencias")
        map_center=[25.66300731045276, -100.35628136471323]
        m=folium.Map(location=map_center,zoom_start=10)
        folium.Marker(location=[25.62376297891402, -100.28856467116765],popup="CREE DIF").add_to(m)
        folium.Marker(location=[25.673218375613313, -100.26305426136842],popup="CAM Especial de Guadalupe").add_to(m)
        folium.Marker(location=[25.600999275525435, -100.26784531347161],popup="TEAP Centro de Diagnóstico Integral").add_to(m)
        st.components.v1.html(m._repr_html_(), height=500)
# Pie de página
st.markdown("---")
st.markdown("© 2024 CREmx. Todos los derechos reservados.")