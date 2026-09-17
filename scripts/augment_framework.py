# -*- coding: utf-8 -*-
import sys

fase_5_1 = """# FASE 5.1 — Telemetría de Respuesta y Speed-to-Lead (Mystery Shopper Pasivo)

Evaluar la fricción inicial y la velocidad de respuesta en los canales públicos de contacto sin completar transacciones ni agendamientos no autorizados.

### 1. Pruebas pasivas de contacto
Registrar:
```text
Click-to-Call mobile: [Funciona enlace tel: directo / Texto plano / Error]
Click-to-SMS / WhatsApp: [Abre canal directo con mensaje precargado / No disponible]
Form field count: [Numero de campos obligatorios]
Triage previo visible: [Califica motivo, presupuesto o urgencia / Formulario ciego]
Auto-responder en tiempo real: [Asistente interactivo / Mensaje generico de espera / Silencio]
```

### 2. Regla de friccion de captura y Speed-to-Lead
* **Longitud de formulario:** Mas de 4 campos en movil reduce la tasa de conversion en un 40%.
* **Lead Decay (Decaimiento de Intencion):**
  * La probabilidad de contactar a un lead calificado cae **8x si la respuesta tarda mas de 5 minutos** (InsideSales / MIT).
  * En servicios premium y salud, la falta de respuesta en los primeros 15 minutos empuja al prospecto directamente a la ficha del competidor mas cercano en Google Maps.

### 3. Escala de Telemetria de Respuesta
```text
- Tier 1 (Instantaneo <2 min): Asistente interactivo o bot conversacional con triage de intencion.
- Tier 2 (Aceptable 2-15 min): Notificacion operativa con respuesta humana rapida.
- Tier 3 (Lento 15-60 min): Riesgo de fuga comercial del 50%.
- Tier 4 (Critico >2 hrs / Silencio): Fuga total; el lead se enfria o compra con la competencia.
```

---

"""

fase_7_1 = """# FASE 7.1 — Auditoría de IA Search, GEO & AEO (2026 Standard)

Evaluar si los motores de busqueda generativa (ChatGPT Search, Perplexity, Gemini, Google AI Overviews, Claude) pueden rastrear, entender, citar y recomendar al prospecto frente a competidores locales.

### 1. Busquedas Generativas de Prueba
Ejecutar en Perplexity y ChatGPT Search (modo web):
```text
"Best [service/specialty] in [City]"
"Top rated [category] near [Neighborhood/City]"
"How much does [core treatment/service] cost at [Business Name]?"
"[Business Name] vs [Top Competitor] reviews and recommendations"
```

Registrar:
```text
Mencion de la marca: [Citado en respuesta directa / Enlaces de fuente / No aparece]
Posicionamiento frente a competidores: [Recomendado como primera opcion / Secundario / Ausente]
Precision de la informacion: [Correcta / Alucinacion de precios / Servicios obsoletos]
Fuentes citadas por la IA: [Web oficial / Google Maps / Yelp / Prensa / Competidor]
```

### 2. Auditoria de Entidad Estructurada y Schema.org
Inspeccionar el codigo fuente del sitio:
```text
Schema LocalBusiness presente: [SI / NO]
Subtipo especifico: [MedicalBusiness / Physician / Restaurant / DaySpa / etc.]
Geo-coordenadas (latitude/longitude): [SI / NO]
openingHoursSpecification: [Coincide exactamente con Google Maps / Discrepancia / Ausente]
hasMenu / makesOffer: [Presente con estructura de servicios y precios / Ausente]
sameAs array: [Vincula perfiles sociales oficiales (IG, FB, GBP, Yelp, LinkedIn) / Ausente]
```

### 3. Senales de IA y llms.txt
```text
robots.txt permite rastreadores de IA: [GPTBot, PerplexityBot, ClaudeBot, Google-Extended permitidos / bloqueados]
llms.txt o llms-full.txt disponible en la raiz: [SI / NO]
Densidad de respuesta directa (Regla de 150 caracteres): [Paginas de servicio explican quien es candidato, procedimiento y recuperacion en el primer parrafo / Prosa generica de marketing]
```

---

"""

h10_1 = """# H10.1 — Back-Office Automation & No-Show Telemetry (Nate Herk Framework)

Auditar los cuellos de botella operativos y la fuga invisible de ingresos post-lead dentro de la clinica o med spa.

### 1. Diagnostico de los 4 Pilares de Automatizacion
Identificar procesos que sean:
* **Repetitive (Repetitivos):** Confirmacion manual de citas una por una por WhatsApp, envio manual de consentimientos informados y cuidados pre/post-operatorios.
* **Time-consuming (Consumen tiempo excesivo):** Copiar y pegar datos de leads de formularios o DMs al software clinico/EHR (Jane, Nextech, Aesthetic Record, GHL).
* **Error-prone (Propensos a error):** Citas agendadas sin tarjeta de credito en garantia o deposito, citas dobles por falta de sincronizacion de calendarios, olvido de seguimiento a los 14 dias (ej. retoque de toxina botulinica).
* **Scalable (Frenan el escalado):** La capacidad de agendar depende al 100% de que la recepcionista este desocupada y en horario de oficina.

### 2. Formula de Fuga por Ausentismo (No-Show ROI Model)
Cuantificar el costo operativo del ausentismo:
```text
Fuga Mensual por No-Shows = (Citas Totales Agendadas / Mes) * (% Tasa de No-Show) * (Ticket Promedio del Tratamiento)
```
*Ejemplo med spa:*
120 citas agendadas/mes * 22% no-show = 26.4 pacientes perdidos.
26.4 * $450 ticket promedio = **$11,880 USD perdidos al mes** en tiempo clinico ocioso.

### 3. Prescripcion Operativa de Sellado
* **Protocolo de 3 Toques Automatizado:**
  1. *Toque 1 (Inmediato):* SMS/WhatsApp de confirmacion con enlace al formulario de historial medico.
  2. *Toque 2 (48 horas antes):* Instrucciones de preparacion y recordatorio interactivo.
  3. *Toque 3 (24 horas antes):* Reconfirmacion con boton interactivo (Confirmar / Reagendar).
* **Micro-deposito de compromiso:** Cobro de $50-$100 reembolsable o acreditable para citas de diagnostico en tratamientos de alto valor.
* **Triage de calificacion rapida:** Filtro de 2 preguntas (motivo principal y ventana de tiempo deseada) para priorizar llamadas del equipo a pacientes listos para comprar.

---

"""

f7_1 = """# F7.1 — Back-Office Friction & Revenue Recovery (Nate Herk Framework)

Auditar la friccion operativa en restaurantes, cafeterias y negocios gastronomicos donde la demanda se pierde tras el primer contacto.

### 1. Diagnostico de los 4 Pilares en Operaciones Gastronomicas
* **Repetitive (Repetitivos):** Responder manualmente en DMs de Instagram y WhatsApp preguntas sobre el menu, opciones veganas/gluten-free, estacionamiento y reservas de grupos.
* **Time-consuming (Consumen tiempo):** Cotizaciones manuales por correo o telefono para eventos privados, cumpleanos o servicio de catering.
* **Error-prone (Propensos a error):** Desincronizacion de precios y disponibilidad entre el menu impreso, Google Maps, la web y plataformas de delivery (DoorDash, Uber Eats).
* **Scalable (Frenan el volumen):** Falta de un canal de fidelizacion directo que permita reactivar clientes en dias lentos (lunes a miercoles).

### 2. Formula de Fuga por Mesa Vacia (No-Show en Restaurantes)
```text
Perdida Semanal por No-Shows = (Mesas Reservadas / Semana) * (% Tasa de Cancelacion / No-Show) * (Ticket Promedio por Mesa)
```

### 3. Prescripcion Operativa de Recuperacion
* **Menu Interactivo y FAQ Automatizado:** Auto-respuesta en Instagram DM / WhatsApp que entrega el menu interactivo, horarios y boton directo de reserva sin intervencion de personal.
* **Cotizador Parametrico de Catering/Eventos:** Formulario inteligente que calcula un estimado aproximado segun el numero de comensales y tipo de evento antes de derivar al gerente.
* **Canal Directo de Fidelizacion:** Base de datos propia de comensales (SMS / Email) para lanzar promociones en dias de baja demanda sin pagar comisiones de plataformas delivery.

---

"""

parte_xiii = """---

# PARTE XIII — EL PUENTE COMERCIAL Y ENTREGA DE LA AUDITORÍA
## Metodología Nate Herk: "Sé un Médico, no un Farmacéutico"

La auditoria tecnica no es un informe para enviar por correo y esperar que el cliente compre. Es la herramienta para liderar una sesion diagnostica de alta autoridad.

### 1. Principio Fundamental
* **Nunca diagnosticar herramientas antes de aislar el cuello de botella:** No hablar de "flujos de n8n", "agentes de IA" o "campanas de anuncios" sin haber demostrado la perdida economica actual.
* **El prospecto compra alivio a una fuga concreta, no software ni horas de servicio.**

### 2. La Regla de Conversacion 75/25
Durante la llamada de entrega de la auditoria:
* **El prospecto habla el 75% del tiempo:** Explica sus dolores operativos, cuantos pacientes/comensales se caen y que frustraciones tiene con su equipo.
* **El consultor habla el 25% del tiempo:** Hace preguntas de calibracion guiadas por los hallazgos de la auditoria y expone la evidencia.

### 3. Estructura de Presentacion en 3 Tiempos

#### Tiempo 1: El Sangrado Inmediato (Quick Wins & Compliance Risk)
* Mostrar los 2 o 3 puntos criticos donde hoy mismo se esta fugando dinero o existe riesgo regulatorio:
  * Botones de llamada o reserva rotos en movil.
  * Claims medicos o de alergenos no respaldados ante FTC/FDA.
  * Respuestas tardias (>2 horas) a leads calificados.
* *Objetivo psicologico:* Establecer urgencia inmediata y credibilidad tecnica.

#### Tiempo 2: El Sellado de Fugas (Infraestructura de Conversion & Triage)
* Presentar la solucion operativa antes de hablar de trafico nuevo:
  * Sistema de pre-calificacion y triage para que el equipo no pierda tiempo con curiosos.
  * Protocolo de reduccion de no-shows mediante recordatorios y depositos automaticos.
  * Captura de resenas para blindar la reputacion en Google Maps e IA Search.
* *Objetivo psicologico:* Demostrar que meter mas trafico en una tuberia rota es desperdiciar dinero.

#### Tiempo 3: La Expansion (Acquisition & Scale)
* Plantear el crecimiento (Meta Ads, Google Ads, SEO) solo como la etapa final una vez que la tasa de conversion y retencion interna esta asegurada.

### 4. Guion de Transicion de la Auditoria a la Propuesta
Al finalizar la revision de los hallazgos:
```text
"Como pudiste ver en la auditoria, tu negocio no tiene un problema de demanda; la gente te busca y llega a tu perfil. El verdadero problema es que tienes fugas en la conversion y en la velocidad de respuesta que te estan costando entre [X] y [Y] dolares al mes.

Nosotros trabajamos bajo dos fases:
Fase 1: Sellamos las fugas operativas (triage, respuesta rapida y reduccion de no-shows).
Fase 2: Escalamos el volumen de adquisicion sabiendo que cada lead que entra se atiende en segundos.

Si estas de acuerdo con este diagnostico, en 48 horas te preparo el plan de trabajo con el cronograma y la inversion exacta. Tiene sentido para ti?"
```

---

"""

filePath = r"f:\EmpathoKnowledge\frameworks\ai-prospect-audit-framework-healthcare-food-services-us.md"
with open(filePath, "r", encoding="utf-8") as f:
    content = f.read()

# Sequential insertion
def insert_before(text, anchor, addition):
    idx = text.find(anchor)
    if idx == -1:
        print(f"FAILED to find anchor: {anchor[:40]}")
        sys.exit(1)
    return text[:idx] + addition + text[idx:]

content = insert_before(content, "# FASE 6", fase_5_1)
content = insert_before(content, "# FASE 8", fase_7_1)
content = insert_before(content, "# H11", h10_1)
content = insert_before(content, "# F8", f7_1)
content = insert_before(content, "# REGLA CRÍTICA", parte_xiii)

with open(filePath, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Framework augmented and written.")
