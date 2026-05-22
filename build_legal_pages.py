import os
import re

cookie_policy_en = """
<h1>Cookie Policy</h1>
<p class="last-updated">Effective Date: May 25, 2026 | Last Updated: May 25, 2026</p>

<h2>1. Introduction</h2>
<p>This Cookie Policy explains how Build Your Castle, Inc., doing business as "Castle" ("Castle," "we," "us," or "our"), uses cookies and similar tracking technologies on our website at <a href="https://buildyourcastle.ai">buildyourcastle.ai</a> and our associated digital services (collectively, the "Site").</p>
<p>By continuing to use our Site, you consent to our use of cookies in accordance with this Cookie Policy, unless you have adjusted your browser settings to refuse cookies. You can manage your cookie preferences at any time as described in Section 6 below.</p>
<p>This Cookie Policy should be read together with our Privacy Policy, which provides additional information about our data practices.</p>

<h2>2. What Are Cookies?</h2>
<p>Cookies are small text files placed on your device (computer, tablet, or smartphone) when you visit a website. They are widely used to make websites work more efficiently, to remember your preferences, and to provide information to website owners about how their sites are being used.</p>
<p>Cookies can be:</p>
<ul>
    <li><strong>Session cookies:</strong> Temporary cookies that are deleted when you close your browser. They help the site function during your visit.</li>
    <li><strong>Persistent cookies:</strong> Cookies that remain on your device for a set period of time or until you delete them. They are used to remember you and your preferences on return visits.</li>
    <li><strong>First-party cookies:</strong> Cookies set directly by Castle when you visit our Site.</li>
    <li><strong>Third-party cookies:</strong> Cookies set by external parties (such as analytics or advertising providers) when you visit our Site.</li>
</ul>
<p>We also use similar technologies such as pixel tags, web beacons, and local storage objects. This Cookie Policy refers to all such technologies collectively as 'cookies.'</p>

<h2>3. Why We Use Cookies</h2>
<p>We use cookies to:</p>
<ul>
    <li>Make our Site work properly and securely;</li>
    <li>Remember your language preference (English or Spanish);</li>
    <li>Remember your cookie consent choices;</li>
    <li>Understand how visitors use our Site and which pages are most popular;</li>
    <li>Measure the effectiveness of our communications and marketing campaigns;</li>
    <li>Personalize your experience and show you content relevant to your interests;</li>
    <li>Prevent fraud and improve security; and</li>
    <li>Improve our Services over time based on usage data.</li>
</ul>

<h2>4. Types of Cookies We Use</h2>
<p>We organize our cookies into four categories:</p>

<h3>4.1 Strictly Necessary Cookies</h3>
<p>These cookies are essential for the Site to function and cannot be switched off in our systems. They are set in response to actions you take, such as setting your cookie preferences, filling in forms, or logging in. Without these cookies, our Site cannot function properly.</p>

<table class="legal-table">
    <thead>
        <tr>
            <th>Cookie Name / Type</th>
            <th>Purpose</th>
            <th>Duration</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>castle_cookie_consent</code></td>
            <td>Stores your cookie consent preferences so we do not ask you again on each visit.</td>
            <td>12 months</td>
        </tr>
        <tr>
            <td><code>castle_lang</code></td>
            <td>Remembers your selected language (English or Spanish).</td>
            <td>12 months</td>
        </tr>
        <tr>
            <td><code>castle_session</code></td>
            <td>Maintains your session while you navigate the Site.</td>
            <td>Session</td>
        </tr>
        <tr>
            <td><code>CSRF token</code></td>
            <td>Prevents cross-site request forgery attacks on form submissions.</td>
            <td>Session</td>
        </tr>
    </tbody>
</table>

<h3>4.2 Functional Cookies</h3>
<p>These cookies enable enhanced functionality and personalization. They may be set by us or by third-party providers whose services we use. If you disable these cookies, some or all of these features may not work properly.</p>

<table class="legal-table">
    <thead>
        <tr>
            <th>Cookie Name / Type</th>
            <th>Purpose</th>
            <th>Duration</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>castle_pref</code></td>
            <td>Remembers your form progress and preferences (e.g., interest selections on the partner form).</td>
            <td>30 days</td>
        </tr>
        <tr>
            <td><code>castle_waitlist_ref</code></td>
            <td>Tracks referral source for waitlist sign-ups to attribute new users correctly.</td>
            <td>30 days</td>
        </tr>
    </tbody>
</table>

<h3>4.3 Analytics and Performance Cookies</h3>
<p>These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our Site. They help us understand which pages are most and least popular and see how visitors move around the Site. All information these cookies collect is aggregated and therefore anonymous.</p>

<table class="legal-table">
    <thead>
        <tr>
            <th>Cookie Name / Type</th>
            <th>Purpose</th>
            <th>Duration</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>_ga</code>, <code>_ga_[ID]</code></td>
            <td>Google Analytics: distinguishes users and tracks page views, session duration, and traffic sources.</td>
            <td>2 years / 1 year</td>
        </tr>
        <tr>
            <td><code>_gid</code></td>
            <td>Google Analytics: distinguishes users on a per-day basis.</td>
            <td>24 hours</td>
        </tr>
        <tr>
            <td><code>_gat</code></td>
            <td>Google Analytics: throttles request rate.</td>
            <td>1 minute</td>
        </tr>
    </tbody>
</table>

<p>Google Analytics is provided by Google LLC. Google processes analytics data on our behalf and may transfer data to the United States. For more information, see Google's Privacy Policy at <a href="https://policies.google.com/privacy" target="_blank">policies.google.com/privacy</a>. You may opt out of Google Analytics by visiting <a href="https://tools.google.com/dlpage/gaoptout" target="_blank">tools.google.com/dlpage/gaoptout</a>.</p>

<h3>4.4 Marketing and Targeting Cookies</h3>
<p>These cookies may be set through our Site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you disable these cookies, you will experience less targeted advertising.</p>

<table class="legal-table">
    <thead>
        <tr>
            <th>Cookie Name / Type</th>
            <th>Purpose</th>
            <th>Duration</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>Meta Pixel (_fbp)</code></td>
            <td>Meta (Facebook/Instagram) Pixel: tracks conversions, ad performance, and builds audiences for marketing.</td>
            <td>3 months</td>
        </tr>
        <tr>
            <td><code>LinkedIn Insight Tag</code></td>
            <td>LinkedIn analytics and conversion tracking for marketing campaigns.</td>
            <td>6 months / 30 days</td>
        </tr>
        <tr>
            <td><code>_gcl_au</code></td>
            <td>Google Ads conversion tracking cookie.</td>
            <td>3 months</td>
        </tr>
    </tbody>
</table>

<p><em>Note: We will only deploy marketing cookies with your prior consent, as required by applicable law (e.g., the EU ePrivacy Directive and GDPR).</em></p>

<h2>5. Third-Party Cookies and Services</h2>
<p>Certain third-party services embedded in our Site may place their own cookies on your device. These include:</p>
<ul>
    <li><strong>Social Media Buttons and Embeds:</strong> Social sharing buttons or embedded content from Instagram, LinkedIn, YouTube, and X (Twitter) may set cookies when you interact with those features. These cookies are subject to the privacy policies of the respective platforms.</li>
    <li><strong>Newsletter Provider:</strong> Our email newsletter service provider may use cookies or tracking pixels in newsletter emails to measure open rates and click-through rates.</li>
    <li><strong>Embedded Forms:</strong> Third-party form or survey tools embedded in our Site may set functional cookies to maintain form state.</li>
</ul>
<p>We do not control these third-party cookies. Please refer to the relevant third-party's privacy and cookie policy for more information.</p>

<h2>6. How to Manage Your Cookie Preferences</h2>
<p>You have several options for managing cookies:</p>

<h3>6.1 Cookie Consent Banner</h3>
<p>When you first visit our Site, you will be presented with a cookie consent banner that allows you to accept or customize your cookie preferences. You can change your preferences at any time by clicking the cookie settings link in the footer of our Site.</p>

<h3>6.2 Browser Settings</h3>
<p>Most web browsers allow you to control cookies through their settings. You can typically:</p>
<ul>
    <li>View what cookies are stored on your device and delete them individually or in bulk;</li>
    <li>Block third-party cookies;</li>
    <li>Block all cookies from specific sites; and</li>
    <li>Block all cookies from being set.</li>
</ul>
<p>Please note that restricting cookies may impact the functionality of our Site. For more information on how to manage cookies in your browser, visit:</p>
<ul>
    <li>Google Chrome: <a href="https://support.google.com/chrome/answer/95647" target="_blank">support.google.com/chrome/answer/95647</a></li>
    <li>Mozilla Firefox: <a href="https://support.mozilla.org/en-US/kb/enable-and-disable-cookies-website-preferences" target="_blank">support.mozilla.org/en-US/kb/enable-and-disable-cookies-website-preferences</a></li>
    <li>Apple Safari: <a href="https://support.apple.com/en-us/guide/safari/sfri11471/mac" target="_blank">support.apple.com/en-us/guide/safari/sfri11471/mac</a></li>
    <li>Microsoft Edge: <a href="https://support.microsoft.com/en-us/microsoft-edge/view-cookies" target="_blank">support.microsoft.com/en-us/microsoft-edge/view-cookies</a></li>
</ul>

<h3>6.3 Opt-Out Tools</h3>
<p>You may also opt out of certain third-party cookies using the following tools:</p>
<ul>
    <li>Google Analytics: <a href="https://tools.google.com/dlpage/gaoptout" target="_blank">tools.google.com/dlpage/gaoptout</a> (browser add-on)</li>
    <li>Meta/Facebook Ads: <a href="https://www.facebook.com/settings?tab=ads" target="_blank">www.facebook.com/settings?tab=ads</a></li>
    <li>LinkedIn Ads: <a href="https://www.linkedin.com/psettings/guest-controls" target="_blank">www.linkedin.com/psettings/guest-controls</a></li>
    <li>Network Advertising Initiative: <a href="https://optout.networkadvertising.org" target="_blank">optout.networkadvertising.org</a></li>
    <li>Digital Advertising Alliance: <a href="https://optout.aboutads.info" target="_blank">optout.aboutads.info</a></li>
</ul>
<p>Please note that opting out of targeted advertising does not mean you will no longer see ads — it means the ads you see will be less tailored to your interests.</p>

<h3>6.4 Do Not Track</h3>
<p>Some browsers include a "Do Not Track" (DNT) feature that signals to websites that you do not want to be tracked. Our Site does not currently respond to DNT signals because there is no industry-wide standard for DNT compliance. We will update this practice if a standard is established.</p>

<h2>7. Updates to This Cookie Policy</h2>
<p>We may update this Cookie Policy from time to time to reflect changes in the cookies we use or for operational, legal, or regulatory reasons. We will notify you of material changes by updating the "Last Updated" date at the top of this policy and, where appropriate, by displaying a notice on our Site.</p>
<p>We encourage you to review this Cookie Policy periodically to stay informed about our use of cookies.</p>

<h2>8. Contact Us</h2>
<p>If you have any questions about our use of cookies or this Cookie Policy, please contact us:</p>
<p class="contact-details">
    <strong>Build Your Castle, Inc.</strong><br>
    Attn: Privacy & Legal Team<br>
    Email: <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a><br>
    Website: <a href="https://buildyourcastle.ai">buildyourcastle.ai</a>
</p>
"""

cookie_policy_es = """
<h1>Política de Cookies</h1>
<p class="last-updated">Fecha de vigencia: 25 de mayo de 2026 | Última actualización: 25 de mayo de 2026</p>

<h2>1. Introducción</h2>
<p>Esta Política de Cookies explica cómo Build Your Castle, Inc., que opera bajo el nombre comercial de "Castle" ("Castle", "nosotros", "nos" o "nuestro"), utiliza cookies y tecnologías de seguimiento similares en nuestro sitio web en <a href="https://buildyourcastle.ai">buildyourcastle.ai</a> y nuestros servicios digitales asociados (colectivamente, el "Sitio").</p>
<p>Al continuar utilizando nuestro Sitio, aceptas nuestro uso de cookies de acuerdo con esta Política de Cookies, a menos que hayas ajustado la configuración de tu navegador para rechazar cookies. Puedes gestionar tus preferencias de cookies en cualquier momento como se describe en la Sección 6 a continuación.</p>
<p>Esta Política de Cookies debe leerse junto con nuestra Política de Privacidad, que proporciona información adicional sobre nuestras prácticas de datos.</p>

<h2>2. ¿Qué son las Cookies?</h2>
<p>Las cookies son pequeños archivos de texto que se colocan en tu dispositivo (computadora, tableta o teléfono inteligente) cuando visitas un sitio web. Se utilizan ampliamente para hacer que los sitios web funcionen de manera más eficiente, recordar tus preferencias y proporcionar información a los propietarios de los sitios sobre cómo se están utilizando.</p>
<p>Las cookies pueden ser:</p>
<ul>
    <li><strong>Cookies de sesión:</strong> Cookies temporales que se eliminan al cerrar el navegador. Ayudan al funcionamiento del sitio durante tu visita.</li>
    <li><strong>Cookies de sesión:</strong> Cookies temporales que se eliminan al cerrar el navegador. Ayudan al funcionamiento del sitio durante tu visita.</li>
    <li><strong>Cookies persistentes:</strong> Cookies que permanecen en tu dispositivo durante un período de tiempo establecido o hasta que las eliminas. Se utilizan para recordarte a ti y tus preferencias en visitas posteriores.</li>
    <li><strong>Cookies de origen:</strong> Cookies establecidas directamente por Castle cuando visitas nuestro Sitio.</li>
    <li><strong>Cookies de terceros:</strong> Cookies establecidas por partes externas (como proveedores de análisis o publicidad) cuando visitas nuestro Sitio.</li>
</ul>
<p>También utilizamos tecnologías similares como etiquetas de píxel, balizas web y objetos de almacenamiento local. Esta Política de Cookies se refiere a todas estas tecnologías colectivamente como 'cookies'.</p>

<h2>3. Por qué utilizamos Cookies</h2>
<p>Utilizamos cookies para:</p>
<ul>
    <li>Hacer que nuestro Sitio funcione correctamente y de forma segura;</li>
    <li>Recordar tu preferencia de idioma (inglés o español);</li>
    <li>Recordar tus elecciones de consentimiento de cookies;</li>
    <li>Entender cómo los visitantes usan nuestro Sitio y qué páginas son más populares;</li>
    <li>Medir la efectividad de nuestras comunicaciones y campañas de marketing;</li>
    <li>Personalizar tu experiencia y mostrarte contenido relevante para tus intereses;</li>
    <li>Prevenir el fraude y mejorar la seguridad; y</li>
    <li>Mejorar nuestros Servicios a lo largo del tiempo basándonos en datos de uso.</li>
</ul>

<h2>4. Tipos de Cookies que utilizamos</h2>
<p>Organizamos nuestras cookies en cuatro categorías:</p>

<h3>4.1 Cookies Estrictamente Necesarias</h3>
<p>Estas cookies son esenciales para que el Sitio funcione y no se pueden desactivar en nuestros sistemas. Se configuran en respuesta a acciones realizadas por ti, como configurar tus preferencias de cookies, completar formularios o iniciar sesión. Sin estas cookies, nuestro Sitio no puede funcionar correctamente.</p>

<table class="legal-table">
    <thead>
        <tr>
            <th>Nombre de la Cookie / Tipo</th>
            <th>Propósito</th>
            <th>Duración</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>castle_cookie_consent</code></td>
            <td>Almacena tus preferencias de consentimiento de cookies para que no te lo volvamos a preguntar en cada visita.</td>
            <td>12 meses</td>
        </tr>
        <tr>
            <td><code>castle_lang</code></td>
            <td>Recuerda tu idioma seleccionado (inglés o español).</td>
            <td>12 meses</td>
        </tr>
        <tr>
            <td><code>castle_session</code></td>
            <td>Mantiene tu sesión mientras navegas por el Sitio.</td>
            <td>Sesión</td>
        </tr>
        <tr>
            <td><code>CSRF token</code></td>
            <td>Previene ataques de falsificación de solicitudes en sitios cruzados en los envíos de formularios.</td>
            <td>Sesión</td>
        </tr>
    </tbody>
</table>

<h3>4.2 Cookies Funcionales</h3>
<p>Estas cookies permiten una funcionalidad y personalización mejoradas. Pueden ser establecidas por nosotros o por proveedores terceros cuyos servicios utilizamos. Si desactivas estas cookies, es posible que algunas o todas estas funciones no funcionen correctamente.</p>

<table class="legal-table">
    <thead>
        <tr>
            <th>Nombre de la Cookie / Tipo</th>
            <th>Propósito</th>
            <th>Duración</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>castle_pref</code></td>
            <td>Recuerda tu progreso en el formulario y tus preferencias (por ejemplo, selecciones de interés en el formulario de socios).</td>
            <td>30 días</td>
        </tr>
        <tr>
            <td><code>castle_waitlist_ref</code></td>
            <td>Realiza el seguimiento de la fuente de referencia para los registros de la lista de espera para atribuir a los nuevos usuarios correctamente.</td>
            <td>30 días</td>
        </tr>
    </tbody>
</table>

<h3>4.3 Cookies de Rendimiento y Análisis</h3>
<p>Estas cookies nos permiten contar las visitas y las fuentes de tráfico para poder medir y mejorar el rendimiento de nuestro Sitio. Nos ayudan a saber qué páginas son las más y menos populares y ver cómo se mueven los visitantes por el Sitio. Toda la información que recopilan estas cookies se agrega y, por lo tanto, es anónima.</p>

<table class="legal-table">
    <thead>
        <tr>
            <th>Nombre de la Cookie / Tipo</th>
            <th>Propósito</th>
            <th>Duración</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>_ga</code>, <code>_ga_[ID]</code></td>
            <td>Google Analytics: distingue a los usuarios y realiza el seguimiento de las visitas a las páginas, la duración de la sesión y las fuentes de tráfico.</td>
            <td>2 años / 1 año</td>
        </tr>
        <tr>
            <td><code>_gid</code></td>
            <td>Google Analytics: distingue a los usuarios de forma diaria.</td>
            <td>24 horas</td>
        </tr>
        <tr>
            <td><code>_gat</code></td>
            <td>Google Analytics: limita el porcentaje de solicitudes.</td>
            <td>1 minuto</td>
        </tr>
    </tbody>
</table>

<p>Google Analytics es proporcionado por Google LLC. Google procesa los datos de análisis en nuestro nombre y puede transferir datos a los Estados Unidos. Para obtener más información, consulta la Política de privacidad de Google en <a href="https://policies.google.com/privacy" target="_blank">policies.google.com/privacy</a>. Puedes optar por no participar en Google Analytics visitando <a href="https://tools.google.com/dlpage/gaoptout" target="_blank">tools.google.com/dlpage/gaoptout</a>.</p>

<h3>4.4 Cookies de Marketing y Segmentación</h3>
<p>Nuestros socios publicitarios pueden establecer estas cookies a través de nuestro Sitio. Estas empresas pueden utilizarlas para crear un perfil de tus intereses y mostrarte anuncios relevantes en otros sitios. No almacenan información personal directamente, sino que se basan en la identificación única de tu navegador y dispositivo de Internet. Si desactivas estas cookies, experimentarás una publicidad menos segmentada.</p>

<table class="legal-table">
    <thead>
        <tr>
            <th>Nombre de la Cookie / Tipo</th>
            <th>Propósito</th>
            <th>Duración</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>Meta Pixel (_fbp)</code></td>
            <td>Píxel de Meta (Facebook/Instagram): realiza el seguimiento de las conversiones, el rendimiento de los anuncios y crea audiencias para marketing.</td>
            <td>3 meses</td>
        </tr>
        <tr>
            <td><code>LinkedIn Insight Tag</code></td>
            <td>Análisis de LinkedIn y seguimiento de conversiones para campañas de marketing.</td>
            <td>6 meses / 30 días</td>
        </tr>
        <tr>
            <td><code>_gcl_au</code></td>
            <td>Cookie de seguimiento de conversiones de Google Ads.</td>
            <td>3 meses</td>
        </tr>
    </tbody>
</table>

<p><em>Nota: Solo utilizaremos cookies de marketing con tu consentimiento previo, según lo requiera la legislación aplicable (por ejemplo, la Directiva de privacidad electrónica de la UE y el RGPD).</em></p>

<h2>5. Cookies y Servicios de Terceros</h2>
<p>Ciertos servicios de terceros integrados en nuestro Sitio pueden colocar sus propias cookies en tu dispositivo. Estos incluyen:</p>
<ul>
    <li><strong>Botones y elementos integrados de redes sociales:</strong> Los botones para compartir en redes sociales o el contenido integrado de Instagram, LinkedIn, YouTube y X (Twitter) pueden configurar cookies al interactuar con esas funciones. Estas cookies están sujetas a las políticas de privacidad de las respectivas plataformas.</li>
    <li><strong>Proveedor de boletines:</strong> Nuestro proveedor de servicios de boletines por correo electrónico puede utilizar cookies o píxeles de seguimiento en los correos electrónicos del boletín para medir las tasas de apertura y de clics.</li>
    <li><strong>Formularios integrados:</strong> Las herramientas de formularios o encuestas de terceros integradas en nuestro Sitio pueden configurar cookies funcionales para mantener el estado del formulario.</li>
</ul>
<p>Nosotros no controlamos estas cookies de terceros. Consulta la política de privacidad y de cookies del tercero correspondiente para obtener más información.</p>

<h2>6. Cómo gestionar tus Preferencias de Cookies</h2>
<p>Tienes varias opciones para gestionar las cookies:</p>

<h3>6.1 Banner de Consentimiento de Cookies</h3>
<p>Cuando visites nuestro Sitio por primera vez, se te presentará un banner de consentimiento de cookies que te permitirá aceptar o personalizar tus preferencias de cookies. Puedes cambiar tus preferencias en cualquier momento haciendo clic en el enlace de configuración de cookies en el pie de página de nuestro Sitio.</p>

<h3>6.2 Configuración del Navegador</h3>
<p>La mayoría de los navegadores web te permiten controlar las cookies a través de su configuración. Normalmente puedes:</p>
<ul>
    <li>Ver qué cookies están almacenadas en tu dispositivo y eliminarlas individualmente o en bloque;</li>
    <li>Bloquear las cookies de terceros;</li>
    <li>Bloquear todas las cookies de sitios específicos; y</li>
    <li>Bloquear la configuración de todas las cookies.</li>
</ul>
<p>Ten en cuenta que restringir las cookies puede afectar la funcionalidad de nuestro Sitio. Para obtener más información sobre cómo gestionar las cookies en tu navegador, visita:</p>
<ul>
    <li>Google Chrome: <a href="https://support.google.com/chrome/answer/95647" target="_blank">support.google.com/chrome/answer/95647</a></li>
    <li>Mozilla Firefox: <a href="https://support.mozilla.org/es-ES/kb/habilitar-y-deshabilitar-cookies-sitios-web-rastrear-preferencias" target="_blank">support.mozilla.org/es-ES/kb/habilitar-y-deshabilitar-cookies-sitios-web-rastrear-preferencias</a></li>
    <li>Apple Safari: <a href="https://support.apple.com/es-es/guide/safari/sfri11471/mac" target="_blank">support.apple.com/es-es/guide/safari/sfri11471/mac</a></li>
    <li>Microsoft Edge: <a href="https://support.microsoft.com/es-es/microsoft-edge/eliminar-y-administrar-cookies" target="_blank">support.microsoft.com/es-es/microsoft-edge/eliminar-y-administrar-cookies</a></li>
</ul>

<h3>6.3 Herramientas de exclusión voluntaria</h3>
<p>También puedes optar por no recibir ciertas cookies de terceros utilizando las siguientes herramientas:</p>
<ul>
    <li>Google Analytics: <a href="https://tools.google.com/dlpage/gaoptout" target="_blank">tools.google.com/dlpage/gaoptout</a> (complemento del navegador)</li>
    <li>Anuncios de Meta/Facebook: <a href="https://www.facebook.com/settings?tab=ads" target="_blank">www.facebook.com/settings?tab=ads</a></li>
    <li>Anuncios de LinkedIn: <a href="https://www.linkedin.com/psettings/guest-controls" target="_blank">www.linkedin.com/psettings/guest-controls</a></li>
    <li>Iniciativa de Publicidad en Red: <a href="https://optout.networkadvertising.org" target="_blank">optout.networkadvertising.org</a></li>
    <li>Alianza de Publicidad Digital: <a href="https://optout.aboutads.info" target="_blank">optout.aboutads.info</a></li>
</ul>
<p>Ten en cuenta que optar por no recibir publicidad segmentada no significa que dejarás de ver anuncios; significa que los anuncios que veas estarán menos adaptados a tus intereses.</p>

<h3>6.4 No Rastrear</h3>
<p>Algunos navegadores include una función de "No rastrear" (DNT) que indica a los sitios web que no deseas que se realice un seguimiento de tu navegación. Nuestro Sitio no responde actualmente a las señales DNT porque no existe un estándar industrial para el cumplimiento de DNT. Actualizaremos esta práctica si se establece un estándar.</p>

<h2>7. Actualizaciones de esta Política de Cookies</h2>
<p>Es posible que actualicemos esta Política de Cookies de vez en cuando para reflejar cambios en las cookies que utilizamos o por razones operativas, legales o reglamentarias. Te notificaremos cualquier cambio sustancial actualizando la fecha de "Última actualización" en la parte superior de esta política y, cuando sea apropiado, mostrando un aviso en nuestro Sitio.</p>
<p>Te recomendamos que revises esta Política de Cookies periódicamente para mantenerte informado sobre nuestro uso de las cookies.</p>

<h2>8. Contacto</h2>
<p>Si tienes alguna pregunta sobre nuestro uso de las cookies o esta Política de Cookies, ponte en contacto con nosotros:</p>
<p class="contact-details">
    <strong>Build Your Castle, Inc.</strong><br>
    A/A: Equipo Legal y de Privacidad<br>
    Correo electrónico: <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a><br>
    Sitio web: <a href="https://buildyourcastle.ai">buildyourcastle.ai</a>
</p>
"""

privacy_policy_en = """
<h1>Privacy Policy</h1>
<p class="last-updated">Effective Date: May 25, 2026 | Last Updated: May 25, 2026</p>

<h2>1. Introduction</h2>
<p>Build Your Castle, Inc., doing business as "Castle" ("Castle," "we," "us," or "our"), is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your personal information when you visit our website at <a href="https://buildyourcastle.ai">buildyourcastle.ai</a> (the "Site"), use our platform, applications, and services (collectively, the "Services"), or interact with us in any other way.</p>
<p>Please read this Privacy Policy carefully. By accessing or using our Services, you acknowledge that you have read, understood, and agree to the practices described in this Privacy Policy. If you do not agree with this Privacy Policy, please do not use our Services.</p>
<p>This Privacy Policy is incorporated into and forms part of our Terms of Use. Capitalized terms used but not defined here have the meanings given in our Terms of Use.</p>

<h2>2. Who We Are</h2>
<p>Castle is an Artificial Intelligence Financial Ecosystem designed to help women build wealth, invest with confidence, and transform their relationship with money. Our platform offers educational content (including live MasterClass Series), an AI-powered Money & Wealth Coach, community cohorts, a curated Investment Marketplace, a Partner Program, and related services. Castle is operated by:</p>
<p class="contact-details">
    <strong>Build Your Castle, Inc.</strong><br>
    A corporation incorporated under the laws of the State of Delaware, United States of America<br>
    Privacy Inquiries: <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a>
</p>

<h2>3. Information We Collect</h2>
<p>We collect information about you in several ways, as described below.</p>

<h3>3.1 Information You Provide Directly</h3>
<p>When you interact with our Services — including joining our waitlist, applying for a MasterClass, registering as a Partner, contacting us, or subscribing to our newsletter — you may provide us with the following categories of personal information:</p>
<ul>
    <li><strong>Identity and Contact Information:</strong> Full name, email address, phone number.</li>
    <li><strong>Demographic Information:</strong> Age range, country of residence.</li>
    <li><strong>Professional Information:</strong> Company or organization name, job title or role.</li>
    <li><strong>Social Media Profiles:</strong> LinkedIn profile URL, Instagram handle or profile link.</li>
    <li><strong>Communications:</strong> Messages, inquiries, and other content you submit through our forms or send directly to us.</li>
    <li><strong>Preferences and Consents:</strong> Your communication preferences and the consents you provide when submitting forms (e.g., consent to receive updates, newsletters, or event notifications).</li>
    <li><strong>Financial Account Information (future feature):</strong> When you choose to integrate external financial accounts with the Castle platform, we may collect financial data, account identifiers, balances, and transaction history as permitted by applicable law and your account provider.</li>
</ul>

<h3>3.2 Information Collected Automatically</h3>
<p>When you visit or use our Services, we and our third-party service providers automatically collect certain technical and usage information, including:</p>
<ul>
    <li><strong>Device and Technical Information:</strong> IP address, browser type and version, operating system, device identifiers, and hardware model.</li>
    <li><strong>Usage Data:</strong> Pages visited, links clicked, time spent on pages, referral URLs, search terms used to find our Site, and other interaction data.</li>
    <li><strong>Location Data:</strong> General geographic location inferred from your IP address (country or region level).</li>
    <li><strong>Cookies and Tracking Technologies:</strong> Information collected through cookies, pixel tags, web beacons, and similar technologies. Please refer to our Cookie Policy for detailed information.</li>
</ul>

<h3>3.3 Information From Third Parties</h3>
<p>We may receive information about you from third parties, including:</p>
<ul>
    <li>Social media platforms (e.g., LinkedIn, Instagram, YouTube, X/Twitter), if you interact with our social media accounts or provide your social media handles.</li>
    <li>Partner organizations, sponsors, or co-promoters who share information about potential platform participants in accordance with their own privacy policies.</li>
    <li>Analytics providers who supply aggregated or de-identified information about usage patterns.</li>
    <li>The Unicoin Foundation and affiliated entities that support the Castle platform, to the extent permitted by applicable law and their respective privacy policies.</li>
</ul>

<h2>4. How We Use Your Information</h2>
<p>We use the personal information we collect for the following purposes:</p>
<ul>
    <li><strong>Providing and Improving Our Services:</strong> To operate the Castle platform, process applications, deliver MasterClass content, match partners, send newsletters, and fulfill your requests.</li>
    <li><strong>Communications:</strong> To send you updates about Castle, the platform launch, MasterClass sessions, community events, and news relevant to women's wealth — but only where you have consented or where we have a legitimate interest to do so.</li>
    <li><strong>Personalization:</strong> To tailor content, recommendations, and the AI Wealth Coach experience to your profile, preferences, and financial goals.</li>
    <li><strong>Analytics and Research:</strong> To understand how users interact with our Services, identify trends, measure the effectiveness of our communications, and improve our platform.</li>
    <li><strong>Marketing:</strong> To send promotional information about Castle products, features, events, and partner offerings, subject to your consent preferences and applicable opt-out rights.</li>
    <li><strong>Security and Fraud Prevention:</strong> To detect, investigate, and prevent fraudulent transactions, abuse, and other unauthorized or harmful activities.</li>
    <li><strong>Legal Compliance:</strong> To comply with applicable laws, regulations, and legal processes, including responding to lawful requests from public authorities.</li>
    <li><strong>Token and Web3 Features:</strong> To manage your participation in the Castle token ecosystem, including tracking token allocations, partnership agreements, and related transactions.</li>
    <li><strong>Business Operations:</strong> To conduct internal business operations, including auditing, financial reporting, and corporate governance.</li>
</ul>

<h2>5. Legal Basis for Processing (GDPR)</h2>
<p>If you are located in the European Economic Area (EEA), the United Kingdom, or another jurisdiction with similar data protection laws, we process your personal data on the following legal bases:</p>
<ul>
    <li><strong>Consent (Article 6(1)(a) GDPR):</strong> Where you have given us explicit consent, for example, to send you marketing communications, newsletters, or to use non-essential cookies.</li>
    <li><strong>Performance of a Contract (Article 6(1)(b) GDPR):</strong> Where processing is necessary to fulfill a contract with you or to take steps at your request prior to entering into a contract (e.g., processing your waitlist application or MasterClass registration).</li>
    <li><strong>Legitimate Interests (Article 6(1)(f) GDPR):</strong> Where processing is necessary for our legitimate interests or those of a third party, provided those interests are not overridden by your rights and interests. This includes platform security, fraud prevention, analytics, improving our services, and internal administrative purposes.</li>
    <li><strong>Legal Obligation (Article 6(1)(c) GDPR):</strong> Where processing is necessary for compliance with a legal obligation to which we are subject.</li>
</ul>
<p>You may withdraw consent at any time where processing is based on consent, without affecting the lawfulness of processing carried out before withdrawal. To withdraw consent, please contact us at <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a>.</p>

<h2>6. How We Share Your Information</h2>
<p>We do not sell your personal information. We may share your information in the following circumstances:</p>
<ul>
    <li><strong>Service Providers:</strong> We share information with trusted third-party vendors and service providers who perform services on our behalf, including email delivery, analytics, hosting, customer support, and payment processing. These providers are contractually obligated to protect your information and use it only for the purposes for which it was disclosed.</li>
    <li><strong>Affiliated Entities:</strong> We may share information with the Unicoin Foundation and other corporate affiliates, to the extent necessary for operating and improving the Castle platform, and subject to appropriate data protection agreements.</li>
    <li><strong>Partner Program Participants:</strong> If you apply to become a Castle Partner (e.g., as an influencer, brand, or expert), relevant aspects of your profile may be shared with our partnership team for evaluation and onboarding purposes.</li>
    <li><strong>Business Transfers:</strong> If Castle is involved in a merger, acquisition, restructuring, sale of assets, or other corporate transaction, your information may be transferred as part of that transaction, subject to the acquirer's commitment to honor this Privacy Policy or notify you of any material changes.</li>
    <li><strong>Legal Requirements:</strong> We may disclose your information if required to do so by law, court order, or government authority, or if we believe in good faith that such disclosure is necessary to protect our rights, the rights of others, or to prevent fraud or harm.</li>
    <li><strong>With Your Consent:</strong> We may share your information for other purposes with your explicit consent.</li>
</ul>

<h2>7. International Data Transfers</h2>
<p>Castle operates from the United States and serves users globally, including from the European Economic Area, the United Kingdom, Latin America, and other regions. When we transfer personal data from the EEA or UK to countries not recognized as providing an adequate level of protection (including the United States), we implement appropriate safeguards, such as Standard Contractual Clauses approved by the European Commission or the UK Information Commissioner's Office (ICO).</p>
<p>By using our Services, you acknowledge that your personal information may be transferred to and processed in the United States or other countries where privacy laws may differ from those in your country of residence.</p>

<h2>8. Data Retention</h2>
<p>We retain personal information for as long as necessary to fulfill the purposes for which it was collected, including to satisfy legal, accounting, or reporting requirements, and to resolve disputes and enforce our agreements.</p>
<p>When your information is no longer needed, we will securely delete or anonymize it. If deletion is not immediately possible (e.g., because information is in backup archives), we will isolate it from further processing until deletion is possible.</p>

<h2>9. Your Privacy Rights</h2>
<p>Depending on your location, you may have the following rights with respect to your personal information:</p>

<h3>9.1 Rights Under GDPR (EEA and UK Users)</h3>
<p>If you are located in the EEA or the UK, you have the following rights under the GDPR or the UK GDPR: Right of Access, Right to Rectification, Right to Erasure ('Right to Be Forgotten'), Right to Restriction of Processing, Right to Data Portability, Right to Object, Right to Withdraw Consent, and the Right to Lodge a Complaint with your national data protection authority (e.g., the Spanish AEPD or UK ICO).</p>

<h3>9.2 Rights Under CCPA/CPRA (California Residents)</h3>
<p>If you are a California resident, the California Consumer Privacy Act (CCPA), as amended by the California Privacy Rights Act (CPRA), grants you the following rights: Right to Know, Right to Delete, Right to Correct, Right to Opt-Out of Sale or Sharing, Right to Limit Use of Sensitive Personal Information, and the Right to Non-Discrimination.</p>

<h3>9.3 Exercising Your Rights</h3>
<p>To exercise any of the rights described in this Section, please contact us by email at <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a>. We may require you to verify your identity before processing your request. We will respond within the timeframes required by applicable law.</p>

<h2>10. Cookies and Tracking Technologies</h2>
<p>We use cookies and similar tracking technologies to enhance your experience on our Services. For detailed information about the types of cookies we use, their purposes, and how to manage your cookie preferences, please refer to our Cookie Policy available at <a href="cookie-policy.html">buildyourcastle.ai/cookie-policy</a>.</p>

<h2>11. Children's Privacy</h2>
<p>Castle's Services are intended for adults aged 18 and older. We do not knowingly collect personal information from individuals under the age of 18. If you are under 18, please do not use our Services or submit any personal information to us. If we become aware that we have inadvertently collected personal information from a child under 18, we will take steps to delete that information as soon as possible.</p>

<h2>12. Artificial Intelligence Features</h2>
<p>Castle's platform incorporates artificial intelligence technologies, including an AI-powered Money & Wealth Coach. When you interact with AI-powered features, we process the information you provide (such as questions, goals, and responses) to generate personalized guidance and recommendations.</p>
<p>You should be aware that:</p>
<ul>
    <li>AI-generated responses are for informational and educational purposes only and do not constitute financial, investment, legal, or professional advice.</li>
    <li>AI outputs may not always be accurate, complete, or suited to your specific circumstances.</li>
    <li>Your interactions with AI features may be reviewed by our team to improve model performance and safety, subject to applicable confidentiality obligations.</li>
</ul>
<p>Castle is not a registered investment adviser, broker-dealer, or financial planner. Nothing in the AI features or elsewhere on the platform should be construed as personalized financial or investment advice.</p>

<h2>13. Web3 and Token-Related Data</h2>
<p>Castle is developing a Web3-powered ecosystem that includes Castle tokens and tokenization features for partners and community members. In connection with these features, we may collect digital wallet addresses, token allocation information, smart contract interaction data, and identity verification information (KYC/AML) required by law.</p>
<p>Blockchain transactions are inherently public and immutable. Information recorded on a public blockchain may not be erasable or modifiable. Castle tokens are not securities or investment products. Participation in the token ecosystem involves risks; please review all applicable disclosures before participating.</p>

<h2>14. Third-Party Links and Services</h2>
<p>Our Services may contain links to third-party websites, social media platforms, and partner services, including LinkedIn, Instagram, YouTube, X (Twitter), the Unicoin Foundation website, and media outlets. This Privacy Policy does not apply to those third-party services. We are not responsible for the content, privacy practices, or data handling of third-party websites or services.</p>

<h2>15. Security</h2>
<p>We implement commercially reasonable administrative, technical, and physical security measures to protect your personal information against unauthorized access, disclosure, alteration, or destruction. However, no method of transmission over the Internet or method of electronic storage is completely secure, and we cannot guarantee its absolute security.</p>

<h2>16. Changes to This Privacy Policy</h2>
<p>We may update this Privacy Policy from time to time to reflect changes in our practices, technology, legal requirements, or for other operational reasons. When we make material changes, we will update the "Last Updated" date at the top of this policy and, where appropriate, notify you by email or by posting a prominent notice on our Site. Your continued use of our Services after any updates constitutes your acknowledgment of the revised Privacy Policy.</p>

<h2>17. EEA/UK Representative and Supervisory Authority</h2>
<p>If you are located in the EEA or UK and have concerns about our data processing practices that we have not been able to resolve to your satisfaction, you have the right to lodge a complaint with the relevant data protection supervisory authority in your country (e.g., the Spanish AEPD or UK ICO).</p>

<h2>18. Contact Us</h2>
<p>If you have any questions, concerns, or requests regarding this Privacy Policy or our privacy practices, please contact us at:</p>
<p class="contact-details">
    <strong>Build Your Castle, Inc.</strong><br>
    Attn: Privacy & Legal Team<br>
    Email: <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a><br>
    Website: <a href="https://buildyourcastle.ai">buildyourcastle.ai</a>
</p>
"""

privacy_policy_es = """
<h1>Política de Privacidad</h1>
<p class="last-updated">Fecha de vigencia: 25 de mayo de 2026 | Última actualización: 25 de mayo de 2026</p>

<h2>1. Introducción</h2>
<p>Build Your Castle, Inc., que opera bajo el nombre comercial de "Castle" ("Castle", "nosotros", "nos" o "nuestro"), se compromete a proteger tu privacidad. Esta Política de Privacidad explica cómo recopilamos, utilizamos, divulgamos y protegemos tu información personal cuando visitas nuestro sitio web en <a href="https://buildyourcastle.ai">buildyourcastle.ai</a> (el "Sitio"), utilizas nuestra plataforma, aplicaciones y servicios (colectivamente, los "Servicios"), o interactúas con nosotros de cualquier otra manera.</p>
<p>Lee esta Política de Privacidad detenidamente. Al acceder o utilizar nuestros Servicios, reconoces que has leído, entendido y aceptas las prácticas descritas en esta Política de Privacidad. Si no estás de acuerdo con esta Política de Privacidad, no utilices nuestros Servicios.</p>
<p>Esta Política de Privacidad se incorpora y forma parte de nuestros Términos de Uso. Los términos en mayúscula utilizados pero no definidos aquí tienen el significado que se les otorga en nuestros Términos de Uso.</p>

<h2>2. Quiénes Somos</h2>
<p>Castle es un Ecosistema Financiero de Inteligencia Artificial diseñado para ayudar a las mujeres a construir riqueza, invertir con confianza y transformar su relación con el dinero. Nuestra plataforma ofrece contenido educativo (incluyendo la serie de MasterClasses en vivo), un Coach de Dinero y Riqueza impulsado por IA, cohortes comunitarias, un Marketplace de Inversiones curado, un Programa de Socios y servicios relacionados. Castle es operado por:</p>
<p class="contact-details">
    <strong>Build Your Castle, Inc.</strong><br>
    Una corporación constituida bajo las leyes del Estado de Delaware, Estados Unidos de América<br>
    Consultas de Privacidad: <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a>
</p>

<h2>3. Información que recopilamos</h2>
<p>Recopilamos información sobre ti de varias maneras, como se describe a continuación.</p>

<h3>3.1 Información que proporcionas directamente</h3>
<p>Cuando interactúas con nuestros Servicios, como unirte a nuestra lista de espera, solicitar una MasterClass, registrarte como Socio, contactarnos o suscribirte a nuestro boletín, puedes proporcionarnos las siguientes categorías de información personal:</p>
<ul>
    <li><strong>Información de identidad y contacto:</strong> Nombre completo, dirección de correo electrónico, número de teléfono.</li>
    <li><strong>Información demográfica:</strong> Rango de edad, país de residencia.</li>
    <li><strong>Información profesional:</strong> Nombre de la empresa u organización, título del puesto o función.</li>
    <li><strong>Perfiles de redes sociales:</strong> URL del perfil de LinkedIn, usuario de Instagram o enlace al perfil.</li>
    <li><strong>Comunicaciones:</strong> Mensajes, consultas y otros contenidos que envíes a través de nuestros formularios o directamente a nosotros.</li>
    <li><strong>Preferencias y consentimientos:</strong> Tus preferencias de comunicación y los consentimientos que proporcionas al enviar formularios (por ejemplo, consentimiento para recibir actualizaciones, boletines o notificaciones de eventos).</li>
    <li><strong>Información de cuenta financiera (característica futura):</strong> Cuando elijas integrar cuentas financieras externas con la plataforma Castle, podemos recopilar datos financieros, identificadores de cuenta, saldos e historial de transacciones según lo permita la ley aplicable y tu proveedor de cuenta.</li>
</ul>

<h3>3.2 Información recopilada automáticamente</h3>
<p>Cuando visitas o utilizas nuestros Servicios, nosotros y nuestros proveedores de servicios externos recopilamos automáticamente cierta información técnica y de uso, incluyendo:</p>
<ul>
    <li><strong>Información técnica y del dispositivo:</strong> Dirección IP, tipo y versión del navegador, sistema operativo, identificadores del dispositivo y modelo de hardware.</li>
    <li><strong>Datos de uso:</strong> Páginas visitadas, enlaces en los que se hizo clic, tiempo dedicado a las páginas, URL de referencia, términos de búsqueda utilizados para encontrar nuestro Sitio y otros datos de interacción.</li>
    <li><strong>Datos de ubicación:</strong> Ubicación geográfica general inferida de tu dirección IP (a nivel de país o región).</li>
    <li><strong>Cookies y tecnologías de seguimiento:</strong> Información recopilada a través de cookies, etiquetas de píxel, balizas web y tecnologías similares. Consulta nuestra Política de Cookies para obtener información detallada.</li>
</ul>

<h3>3.3 Información de terceros</h3>
<p>Podemos recibir información sobre ti de terceros, incluyendo:</p>
<ul>
    <li>Plataformas de redes sociales (por ejemplo, LinkedIn, Instagram, YouTube, X/Twitter), si interactúas con nuestras cuentas de redes sociales o proporcionas tus usuarios de redes sociales.</li>
    <li>Organizaciones asociadas, patrocinadores o co-promotores que comparten información sobre posibles participantes de la plataforma de acuerdo con sus propias políticas de privacidad.</li>
    <li>Proveedores de análisis que suministran información agregada o desidentificada sobre los patrones de uso.</li>
    <li>La Fundación Unicoin y entidades afiliadas que apoyan la plataforma Castle, en la medida permitida por la ley aplicable y sus respectivas políticas de privacidad.</li>
</ul>

<h2>4. Cómo utilizamos tu información</h2>
<p>Utilizamos la información personal que recopilamos para los siguientes propósitos:</p>
<ul>
    <li><strong>Proporcionar y mejorar nuestros Servicios:</strong> Para operar la plataforma Castle, procesar solicitudes, entregar el contenido de la MasterClass, conectar socios, enviar boletines y cumplir con tus solicitudes.</li>
    <li><strong>Comunicaciones:</strong> Para enviarte actualizaciones sobre Castle, el lanzamiento de la plataforma, sesiones de MasterClass, eventos comunitarios y noticias relevantes sobre la riqueza de las mujeres, pero solo cuando hayas dado tu consentimiento o cuando tengamos un interés legítimo para hacerlo.</li>
    <li><strong>Personalización:</strong> Para adaptar el contenido, las recomendaciones y la experiencia del Coach de Riqueza de IA a tu perfil, preferencias y objetivos financieros.</li>
    <li><strong>Análisis e investigación:</strong> Para entender cómo los usuarios interactúan con nuestros Servicios, identificar tendencias, medir la efectividad de nuestras comunicaciones y mejorar nuestra plataforma.</li>
    <li><strong>Marketing:</strong> Para enviar información promocional sobre los productos, características, eventos y ofertas de socios de Castle, sujeto a tus preferencias de consentimiento y derechos de exclusión aplicables.</li>
    <li><strong>Seguridad y prevención del fraude:</strong> Para detectar, investigar y prevenir transacciones fraudulentas, abusos y otras actividades no autorizadas o perjudiciales.</li>
    <li><strong>Cumplimiento legal:</strong> Para cumplir con las leyes, regulaciones y procesos legales aplicables, incluyendo responder a solicitudes legítimas de las autoridades públicas.</li>
    <li><strong>Características de Tokens y Web3:</strong> Para gestionar tu participación en el ecosistema de tokens de Castle, incluyendo el seguimiento de las asignaciones de tokens, acuerdos de asociación y transacciones relacionadas.</li>
    <li><strong>Operaciones comerciales:</strong> Para llevar a cabo operaciones comerciales internas, incluyendo auditorías, informes financieros y gobierno corporativo.</li>
</ul>

<h2>5. Base legal para el procesamiento (RGPD)</h2>
<p>Si te encuentras en el Espacio Económico Europeo (EEE), el Reino Unido u otra jurisdicción con leyes de protección de datos similares, procesamos tus datos personales sobre las siguientes bases legales:</p>
<ul>
    <li><strong>Consentimiento (Artículo 6(1)(a) RGPD):</strong> Cuando nos has dado tu consentimiento explícito, por ejemplo, para enviarte comunicaciones de marketing, boletines o para utilizar cookies no esenciales.</li>
    <li><strong>Ejecución de un contrato (Artículo 6(1)(b) RGPD):</strong> Cuando el procesamiento es necesario para cumplir con un contrato contigo o para tomar medidas a petición tuya antes de celebrar un contrato (por ejemplo, procesar tu solicitud de lista de espera o registro de MasterClass).</li>
    <li><strong>Intereses legítimos (Artículo 6(1)(f) RGPD):</strong> Cuando el procesamiento es necesario para nuestros intereses legítimos o los de un tercero, siempre que dichos intereses no queden anulados por tus derechos e intereses. Esto incluye la seguridad de la plataforma, la prevención del fraude, el análisis, la mejora de nuestros servicios y fines administrativos internos.</li>
    <li><strong>Obligación legal (Artículo 6(1)(c) RGPD):</strong> Cuando el procesamiento es necesario para el cumplimiento de una obligación legal a la que estamos sujetos.</li>
</ul>
<p>Puedes retirar tu consentimiento en cualquier momento cuando el procesamiento se base en el consentimiento, sin que ello afecte a la licitud del procesamiento realizado antes de la retirada. Para retirar tu consentimiento, ponte en contacto con nosotros en <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a>.</p>

<h2>6. Cómo compartimos tu información</h2>
<p>No vendemos tu información personal. Podemos compartir tu información en las siguientes circunstancias:</p>
<ul>
    <li><strong>Proveedores de servicios:</strong> Compartimos información con proveedores externos de confianza que realizan servicios en nuestro nombre, incluyendo envío de correos electrónicos, análisis, alojamiento, soporte al cliente y procesamiento de pagos. Estos proveedores están obligados contractualmente a proteger tu información y a utilizarla únicamente para los fines para los que fue divulgada.</li>
    <li><strong>Entidades afiliadas:</strong> Podemos compartir información con la Fundación Unicoin y otras filiales corporativas, en la medida necesaria para operar y mejorar la plataforma Castle, y sujeto a los acuerdos de protección de datos adecuados.</li>
    <li><strong>Participantes del programa de socios:</strong> Si solicitas convertirte en Socio de Castle (por ejemplo, como influencer, marca o experto), los aspectos relevantes de tu perfil pueden compartirse con nuestro equipo de asociaciones para fines de evaluación e incorporación.</li>
    <li><strong>Transferencias comerciales:</strong> Si Castle participa en una fusión, adquisición, reestructuración, venta de activos u otra transacción corporativa, tu información puede ser transferida como parte de esa transacción, sujeto al compromiso del adquirente de respetar esta Política de Privacidad o de notificarte cualquier cambio sustancial.</li>
    <li><strong>Requisitos legales:</strong> Podemos divulgar tu información si la ley, una orden judicial o una autoridad gubernamental así lo requieren, o si creemos de buena fe que dicha divulgación es necesaria para proteger nuestros derechos, los derechos de otros o para prevenir el fraude o daños.</li>
    <li><strong>Con tu consentimiento:</strong> Podemos compartir tu información para otros fines con tu consentimiento explícito.</li>
</ul>

<h2>7. Transferencias internacionales de datos</h2>
<p>Castle opera desde los Estados Unidos y atiende a usuarios de todo el mundo, incluidos los del Espacio Económico Europeo, el Reino Unido, América Latina y otras regiones. Cuando transferimos datos personales del EEE o del Reino Unido a países que no se reconoce que proporcionen un nivel adecuado de protección (incluidos los Estados Unidos), implementamos las salvaguardas adecuadas, como las Cláusulas Contractuales Tipo aprobadas por la Comisión Europea o la Oficina del Comisionado de Información del Reino Unido (ICO).</p>
<p>Al utilizar nuestros Servicios, reconoces que tu información personal puede ser transferida y procesada en los Estados Unidos o en otros países donde las leyes de privacidad pueden diferir de las de tu país de residencia.</p>

<h2>8. Retención de datos</h2>
<p>Retenemos la información personal durante el tiempo que sea necesario para cumplir con los fines para los que fue recopilada, incluso para cumplir con los requisitos legales, contables o de presentación de informes, y para resolver disputas y hacer cumplir nuestros acuerdos.</p>
<p>Cuando tu información ya no sea necesaria, la eliminaremos de forma segura o la anonimizaremos. Si la eliminación no es posible de inmediato (por ejemplo, porque la información se encuentra en archivos de copia de seguridad), la aislaremos de cualquier procesamiento posterior hasta que sea posible su eliminación.</p>

<h2>9. Tus derechos de privacidad</h2>
<p>Dependiendo de tu ubicación, puedes tener los siguientes derechos con respecto a tu información personal:</p>

<h3>9.1 Derechos bajo el RGPD (Usuarios del EEE y del Reino Unido)</h3>
<p>Si te encuentras en el EEE o en el Reino Unido, tienes los siguientes derechos bajo el RGPD o el RGPD del Reino Unido: Derecho de acceso, Derecho de rectificación, Derecho de supresión ("Derecho al olvido"), Derecho a la limitación del procesamiento, Derecho a la portabilidad de los datos, Derecho de oposición, Derecho a retirar el consentimiento, y el Derecho a presentar una reclamación ante tu autoridad nacional de protección de datos (por ejemplo, la AEPD española o la ICO del Reino Unido).</p>

<h3>9.2 Derechos bajo la CCPA/CPRA (Residentes de California)</h3>
<p>Si eres residente de California, la Ley de Privacidad del Consumidor de California (CCPA), en su versión modificada por la Ley de Derechos de Privacidad de California (CPRA), te otorga los siguientes derechos: Derecho a saber, Derecho a eliminar, Derecho a corregir, Derecho a excluirte de la venta o el intercambio, Derecho a limitar el uso de información personal confidencial, y el Derecho a la no discriminación.</p>

<h3>9.3 Ejercicio de tus derechos</h3>
<p>Para ejercer cualquiera de los derechos descritos en esta Sección, ponte en contacto con nosotros por correo electrónico en <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a>. Es posible que te solicitemos que verifiques tu identidad antes de procesar tu solicitud. Responderemos dentro de los plazos exigidos por la ley aplicable.</p>

<h2>10. Cookies y tecnologías de seguimiento</h2>
<p>Utilizamos cookies y tecnologías de seguimiento similares para mejorar tu experiencia en nuestros Servicios. Para obtener información detallada sobre los tipos de cookies que utilizamos, sus fines y cómo gestionar tus preferencias de cookies, consulta nuestra Política de Cookies disponible en <a href="cookie-policy_es.html">buildyourcastle.ai/cookie-policy</a>.</p>

<h2>11. Privacidad de los niños</h2>
<p>Los Servicios de Castle están destinados a adultos mayores de 18 años. No recopilamos a sabiendas información personal de personas menores de 18 años. Si eres menor de 18 años, no utilices nuestros Servicios ni nos envíes información personal. Si nos percatamos de que hemos recopilado inadvertidamente información personal de un menor de 18 años, tomaremos medidas para eliminar esa información lo antes posible.</p>

<h2>12. Funciones de Inteligencia Artificial</h2>
<p>La plataforma de Castle incorpora tecnologías de inteligencia artificial, incluido un Coach de Dinero y Riqueza impulsado por IA. Cuando interactúas con funciones impulsadas por IA, procesamos la información que proporcionas (como preguntas, objetivos y respuestas) para generar orientación y recomendaciones personalizadas.</p>
<p>Debes tener en cuenta que:</p>
<ul>
    <li>Las respuestas generadas por IA son solo para fines informativos y educativos y no constituyen asesoramiento financiero, de inversión, legal o profesional.</li>
    <li>Los resultados de la IA pueden no ser siempre precisos, completos o adecuados para tus circunstancias específicas.</li>
    <li>Tus interacciones con las funciones de IA pueden ser revisadas por nuestro equipo para mejorar el rendimiento y la seguridad del modelo, sujeto a las obligaciones de confidencialidad aplicables.</li>
</ul>
<p>Castle no es un asesor de inversiones registrado, un agente de bolsa o un planificador financiero. Nada en las funciones de IA ni en ningún otro lugar de la plataforma debe interpretarse como asesoramiento financiero o de inversión personalizado.</p>

<h2>13. Datos relacionados con Web3 y Tokens</h2>
<p>Castle está desarrollando un ecosistema impulsado por Web3 que incluye tokens de Castle y características de tokenización para socios y miembros de la comunidad. En relación con estas características, podemos recopilar direcciones de billeteras digitales, información de asignación de tokens, datos de interacción de contratos inteligentes e información de verificación de identidad (KYC/AML) requerida por la ley.</p>
<p>Las transacciones en blockchain son inherentemente públicas e inmutables. La información registrada en una blockchain pública puede no ser borrable o modificable. Los tokens de Castle no son valores ni productos de inversión. La participación en el ecosistema de tokens implica riesgos; revisa todas las divulgaciones aplicables antes de participar.</p>

<h2>14. Enlaces y servicios de terceros</h2>
<p>Nuestros Servicios pueden contener enlaces a sitios web de terceros, plataformas de redes sociales y servicios de socios, incluidos LinkedIn, Instagram, YouTube, X (Twitter), el sitio web de la Fundación Unicoin y medios de comunicación. Esta Política de Privacidad no se aplica a esos servicios de terceros. No somos responsables del contenido, las prácticas de privacidad o el manejo de datos de sitios web o servicios de terceros.</p>

<h2>15. Seguridad</h2>
<p>Implementamos medidas de seguridad administrativas, técnicas y físicas comercialmente razonables para proteger tu información personal contra el acceso, la divulgación, la alteración o la destrucción no autorizados. Sin embargo, ningún método de transmisión a través de Internet o método de almacenamiento electrónico es completamente seguro, y no podemos garantizar su seguridad absoluta.</p>

<h2>16. Cambios en esta Política de Privacidad</h2>
<p>Pueden actualizar esta Política de Privacidad de vez en cuando para reflejar cambios en nuestras prácticas, tecnología, requisitos legales o por otras razones operativas. Cuando realicemos cambios significativos, actualizaremos la fecha de "Última actualización" en la parte superior de esta política y, cuando sea apropiado, te lo notificaremos por correo electrónico o mediante un aviso destacado en nuestro Sitio. Tu uso continuado de nuestros Servicios después de cualquier actualización constituye tu aceptación de la Política de Privacidad revisada.</p>

<h2>17. Representante en el EEE/Reino Unido y Autoridad de Control</h2>
<p>Si te encuentras en el EEE o en el Reino Unido y tienes inquietudes sobre nuestras prácticas de procesamiento de datos que no hayamos podido resolver a tu satisfacción, tienes derecho a presentar una reclamación ante la autoridad de control de protección de datos correspondiente en tu país (por ejemplo, la AEPD española o la ICO del Reino Unido).</p>

<h2>18. Contacto</h2>
<p>Si tienes alguna pregunta, inquietud o solicitud con respecto a esta Política de Privacidad o a nuestras prácticas de privacidad, ponte en contacto con nosotros en:</p>
<p class="contact-details">
    <strong>Build Your Castle, Inc.</strong><br>
    A/A: Equipo Legal y de Privacidad<br>
    Correo electrónico: <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a><br>
    Sitio web: <a href="https://buildyourcastle.ai">buildyourcastle.ai</a>
</p>
"""

terms_of_use_en = """
<h1>Terms of Use</h1>
<p class="last-updated">Effective Date: May 25, 2026 | Last Updated: May 25, 2026</p>

<h2>1. Acceptance of These Terms</h2>
<p>These Terms of Use ("Terms") constitute a legally binding agreement between you and Build Your Castle, Inc., a Delaware corporation doing business as "Castle" ("Castle," "we," "us," or "our"), governing your access to and use of our website at <a href="https://buildyourcastle.ai">buildyourcastle.ai</a>, our platform, mobile applications, AI-powered tools, educational content, and all related services (collectively, the "Services").</p>
<p><strong>BY ACCESSING OR USING THE SERVICES, YOU CONFIRM THAT YOU HAVE READ, UNDERSTOOD, AND AGREE TO BE BOUND BY THESE TERMS AND OUR PRIVACY POLICY AND COOKIE POLICY, WHICH ARE INCORPORATED HEREIN BY REFERENCE. IF YOU DO NOT AGREE TO THESE TERMS, YOU MUST NOT USE THE SERVICES.</strong></p>
<p>If you are accessing or using the Services on behalf of a company, organization, or other legal entity, you represent that you have the authority to bind that entity to these Terms, in which case "you" refers to that entity.</p>

<h2>2. Changes to These Terms</h2>
<p>We reserve the right to modify these Terms at any time. When we make material changes, we will update the "Last Updated" date at the top of these Terms and, where appropriate, notify you by email or by posting a notice on our Site. Your continued use of the Services after any changes become effective constitutes your acceptance of the revised Terms.</p>
<p>We encourage you to review these Terms periodically. If you do not agree to the modified Terms, you must stop using the Services.</p>

<h2>3. Eligibility</h2>
<p>To use the Services, you must:</p>
<ul>
    <li>Be at least 18 years of age (or the age of majority in your jurisdiction, whichever is older);</li>
    <li>Have the legal capacity to enter into binding contracts under the laws of your jurisdiction;</li>
    <li>Not be prohibited from using the Services under applicable law; and</li>
    <li>Agree to and comply with these Terms.</li>
</ul>
<p>Castle's Services are designed for adult women who wish to build financial literacy and wealth. However, the Services are available to all adults who meet the eligibility requirements above. By using the Services, you represent and warrant that you meet all of the above requirements. If you do not meet these requirements, you must not access or use the Services.</p>

<h2>4. Description of Services</h2>
<p>Castle provides an Artificial Intelligence Financial Ecosystem designed to help women transform their relationship with money and build wealth. The Services currently include, and may in the future expand to include, the following:</p>

<h3>4.1 Waitlist and Community</h3>
<p>Castle operates a waitlist for prospective users who wish to be among the first to access the platform. By joining the waitlist, you provide us with contact information and agree to receive updates and announcements about the Castle platform.</p>

<h3>4.2 MasterClass Series</h3>
<p>Castle offers a live MasterClass Series focused on financial education, wealth mindset, and investment strategies. MasterClass participation is by application only, subject to availability, and subject to separate program terms communicated to accepted applicants. The MasterClass Series is currently offered free of charge, though this may change in the future. Castle reserves the right to modify, suspend, or discontinue any MasterClass program at any time.</p>

<h3>4.3 AI Money & Wealth Coach</h3>
<p>Castle's platform incorporates an AI-powered Money & Wealth Coach that provides personalized financial guidance, educational content, and goal-tracking tools. By interacting with the AI Coach, you acknowledge that the AI Coach provides information for educational and informational purposes only; AI-generated content does not constitute financial, investment, legal, tax, or professional advice; you should not rely solely on AI-generated content when making financial decisions; and AI outputs may not be accurate, complete, or appropriate for your specific circumstances.</p>

<h3>4.4 Account Integration (Future Feature)</h3>
<p>Castle plans to offer account integration features that allow you to connect external financial accounts (such as bank accounts, brokerage accounts, or other financial platforms) to view and analyze your financial picture in one place. When this feature becomes available, additional terms and disclosures will apply.</p>

<h3>4.5 Investment Marketplace (Future Feature)</h3>
<p>Castle plans to offer an Investment Marketplace where curated investment opportunities may be presented to eligible users. When and if the Investment Marketplace is made available, it will be subject to separate terms, conditions, and regulatory disclosures. Participation in the Investment Marketplace will require your acknowledgment of specific risk disclosures and applicable eligibility requirements.</p>

<h3>4.6 Partner Program</h3>
<p>Castle offers a Partner Program for influencers, content creators, brands, women's organizations, and experts who wish to collaborate with Castle. Participation in the Partner Program is subject to a separate Partner Agreement and related terms communicated during the application and onboarding process.</p>

<h3>4.7 Newsletter and Communications</h3>
<p>With your consent, Castle sends newsletters, platform updates, event notifications, and other communications. You may unsubscribe from marketing communications at any time by clicking the 'unsubscribe' link in any email or by contacting us at <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a>.</p>

<h2>5. User Registration and Accounts</h2>
<p>To access certain features of the Services, you may be required to create an account or submit registration information through our forms. When you register or submit information, you agree to: provide accurate, current, and complete information; maintain and promptly update your information; maintain the security and confidentiality of any account credentials; notify us immediately of any unauthorized use of your account at <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a>; and accept responsibility for all activities that occur under your account.</p>
<p>Castle reserves the right to suspend or terminate your account if any information provided is found to be inaccurate, false, outdated, or incomplete, or if you violate these Terms.</p>

<h2>6. User Conduct</h2>
<p>By using the Services, you agree not to: use the Services for any unlawful purpose; impersonate any person or entity; upload or transmit defamatory, obscene, offensive, threatening, or harassing content; engage in conduct that restricts or inhibits anyone's use of the Services; use automated means to access the Services; attempt to gain unauthorized access to our systems; transmit viruses or malicious code; interfere with the performance of the Services; send spam; violate intellectual property rights; or engage in market manipulation or fraudulent financial activity.</p>

<h2>7. No Financial Advice — Important Disclaimer</h2>
<p><strong>IMPORTANT: CASTLE IS NOT A REGISTERED INVESTMENT ADVISER, BROKER-DEALER, FINANCIAL PLANNER, FINANCIAL ANALYST, OR FIDUCIARY. NOTHING ON THE CASTLE PLATFORM — INCLUDING THE AI WEALTH COACH, EDUCATIONAL CONTENT, MASTERCLASS SERIES, NEWSLETTERS, PARTNER COMMUNICATIONS, OR ANY OTHER SERVICE — CONSTITUTES FINANCIAL, INVESTMENT, TAX, LEGAL, OR PROFESSIONAL ADVICE OF ANY KIND.</strong></p>
<p>All content, tools, educational materials, and AI-generated outputs provided through the Services are for general informational and educational purposes only. They do not constitute and should not be relied upon as a substitute for professional financial, investment, tax, legal, or other advice tailored to your individual circumstances.</p>
<p>Before making any financial or investment decision, you should consult a qualified financial adviser, investment adviser, tax professional, attorney, or other licensed professional who can evaluate your specific situation, risk tolerance, and objectives.</p>
<p>Castle makes no representation or warranty about the suitability of any investment opportunity, financial strategy, or course of action for any particular user. Past performance of any investment discussed or referenced on the platform is not indicative of future results. All investments involve risk, including the possible loss of principal.</p>

<h2>8. Intellectual Property</h2>
<h3>8.1 Castle's Intellectual Property</h3>
<p>All content, materials, features, and functionality on the Services — including text, graphics, logos, icons, images, audio/video clips, the Castle name and brand, and overall look and feel — are owned by Build Your Castle, Inc. or its licensors and are protected by United States and international copyright, trademark, patent, trade secret, and other intellectual property laws.</p>
<p>You may not copy, reproduce, distribute, modify, create derivative works of, or transmit any content from the Services without our express prior written consent, except for personal, non-commercial transitory viewing or personal non-commercial use.</p>

<h3>8.2 User-Generated Content</h3>
<p>If you submit, post, or transmit any content through the Services, you grant Castle a non-exclusive, worldwide, royalty-free, perpetual, irrevocable license to use, reproduce, modify, adapt, publish, translate, and display such content in connection with operating and improving the Services, subject to our Privacy Policy.</p>

<h3>8.3 Feedback</h3>
<p>If you provide Castle with any feedback, suggestions, or ideas regarding the Services, you grant Castle an unrestricted, royalty-free, perpetual license to use and incorporate such Feedback without any obligation to you.</p>

<h2>9. Artificial Intelligence Features and Content</h2>
<p>Castle's Services incorporate artificial intelligence technologies. You acknowledge and agree that AI-generated outputs are produced algorithmically and may not always be accurate or current; Castle does not guarantee the accuracy of AI content; you assume sole responsibility for decisions made based on AI outputs; Castle may use interactions to improve performance subject to our Privacy Policy; and AI features may be modified or discontinued at any time.</p>

<h2>10. Web3, Blockchain, and Castle Token Features</h2>
<p>Castle is developing a Web3-powered ecosystem that includes blockchain-based tokens ("Castle Tokens"). By participating, you acknowledge and agree that:</p>
<p><strong>CASTLE TOKENS ARE NOT SECURITIES, INVESTMENT PRODUCTS, OR FINANCIAL INSTRUMENTS. THEY ARE NOT OFFERED OR SOLD AS INVESTMENTS AND CONFER NO OWNERSHIP INTEREST, DIVIDEND RIGHTS, VOTING RIGHTS, OR OTHER FINANCIAL ENTITLEMENTS IN BUILD YOUR CASTLE, INC. OR ANY AFFILIATED ENTITY.</strong></p>
<p>Blockchain transactions are irreversible and immutable. The value of digital tokens may decline to zero. You are responsible for compliance with the laws of your jurisdiction. Castle reserves the right to modify or discontinue token features, and smart contracts are provided 'as is.'</p>

<h2>11. Third-Party Links, Content, and Services</h2>
<p>The Services may contain links to, or integrate with, third-party websites or services (e.g., social media, Unicoin Foundation, investment platforms). We do not endorse or control third-party content or services, and shall not be responsible or liable for any damage or loss caused in connection with them.</p>

<h2>12. Disclaimer of Warranties</h2>
<p><strong>THE SERVICES ARE PROVIDED ON AN 'AS IS' AND 'AS AVAILABLE' BASIS, WITHOUT ANY WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED. TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, CASTLE EXPRESSLY DISCLAIMS ALL WARRANTIES, INCLUDING IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.</strong></p>

<h2>13. Limitation of Liability</h2>
<p><strong>TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, IN NO EVENT WILL CASTLE, ITS AFFILIATES, OFFICERS, DIRECTORS, EMPLOYEES, OR AGENTS BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, PUNITIVE, OR EXEMPLARY DAMAGES, INCLUDING LOSS OF PROFITS, REVENUE, DATA, OR USE.</strong></p>
<p><strong>CASTLE'S TOTAL CUMULATIVE LIABILITY TO YOU FOR ALL CLAIMS WILL NOT EXCEED THE GREATER OF THE AMOUNT YOU PAID TO CASTLE IN THE PRECEDING TWELVE MONTHS OR ONE HUNDRED U.S. DOLLARS (USD $100).</strong></p>

<h2>14. Indemnification</h2>
<p>You agree to defend, indemnify, and hold harmless Build Your Castle, Inc., its affiliates, officers, directors, and employees from and against any claims, liabilities, damages, losses, and expenses (including attorney's fees) arising out of or in connection with your use of the Services, your violation of these Terms, or your violation of any rights of another party.</p>

<h2>15. Governing Law and Dispute Resolution</h2>
<h3>15.1 Governing Law</h3>
<p>These Terms are governed by and construed in accordance with the laws of the State of Delaware, United States of America, without regard to conflict of law principles.</p>

<h3>15.2 Informal Resolution</h3>
<p>Before initiating formal legal action, you agree to first contact Castle at <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a> to attempt informal dispute resolution for a period of 30 days.</p>

<h3>15.3 Arbitration</h3>
<p>Any unresolved dispute shall be settled by binding arbitration administered by the American Arbitration Association (AAA) under its Consumer Arbitration Rules. The arbitration will be conducted in English.</p>

<h3>15.4 Class Action Waiver</h3>
<p><strong>YOU AND CASTLE AGREE THAT EACH PARTY MAY BRING CLAIMS AGAINST THE OTHER ONLY IN YOUR OR ITS INDIVIDUAL CAPACITY AND NOT AS A PLAINTIFF OR CLASS MEMBER IN ANY PURPORTED CLASS OR REPRESENTATIVE ACTION.</strong></p>

<h2>16. Term and Termination</h2>
<p>These Terms remain in effect until terminated. Castle may terminate or suspend your access to the Services at any time, with or without cause or notice. Upon termination, your right to use the Services ceases immediately.</p>

<h2>17. Modifications to the Services</h2>
<p>Castle reserves the right to modify, suspend, or discontinue any aspect of the Services at any time without notice or liability.</p>

<h2>18. General Provisions</h2>
<p>These Terms, together with our Privacy Policy and Cookie Policy, constitute the entire agreement between you and Castle. If any provision is found to be invalid, the remaining provisions continue in effect. You may not assign these Terms, but Castle may do so freely. These Terms are written in English, and any translation is for convenience only.</p>

<h2>19. Contact Us</h2>
<p>If you have any questions, concerns, or feedback about these Terms, please contact us:</p>
<p class="contact-details">
    <strong>Build Your Castle, Inc.</strong><br>
    Attn: Legal Team<br>
    Email: <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a><br>
    Website: <a href="https://buildyourcastle.ai">buildyourcastle.ai</a>
</p>
"""

terms_of_use_es = """
<h1>Términos de Uso</h1>
<p class="last-updated">Fecha de vigencia: 25 de mayo de 2026 | Última actualización: 25 de mayo de 2026</p>

<h2>1. Aceptación de estos Términos</h2>
<p>Estos Términos de Uso ("Términos") constituyen un acuerdo legalmente vinculante entre tú y Build Your Castle, Inc., una corporación de Delaware que opera bajo el nombre comercial de "Castle" ("Castle", "nosotros", "nos" o "nuestro"), que rige tu acceso y uso de nuestro sitio web en <a href="https://buildyourcastle.ai">buildyourcastle.ai</a>, nuestra plataforma, aplicaciones móviles, herramientas impulsadas por IA, contenido educativo y todos los servicios relacionados (colectivamente, los "Servicios").</p>
<p><strong>AL ACCEDER O UTILIZAR LOS SERVICIOS, CONFIRMAS QUE HAS LEÍDO, ENTENDIDO Y ACEPTAS ESTAR VINCULADO POR ESTOS TÉRMINOS Y NUESTRA POLÍTICA DE PRIVACIDAD Y POLÍTICA DE COOKIES, QUE SE INCORPORAN AQUÍ POR REFERENCIA. SI NO ACEPTAS ESTOS TÉRMINOS, NO DEBES UTILIZAR LOS SERVICIOS.</strong></p>
<p>Si estás accediendo o utilizando los Servicios en nombre de una empresa, organización u otra entidad legal, declaras que tienes la autoridad para vincular a esa entidad a estos Términos, en cuyo caso "tú" se refiere a esa entidad.</p>

<h2>2. Cambios en estos Términos</h2>
<p>Nos reservamos el derecho de modificar estos Términos en cualquier momento. Cuando realicemos cambios significativos, actualizaremos la fecha de "Última actualización" en la parte superior de estos Términos y, cuando sea apropiado, te lo notificaremos por correo electrónico o mediante un aviso en nuestro Sitio. Tu uso continuado de los Servicios después de que los cambios entren en vigencia constituye tu aceptación de los Términos revisados.</p>
<p>Te recomendamos que revises estos Términos periódicamente. Si no estás de acuerdo con los Términos modificados, debes dejar de utilizar los Servicios.</p>

<h2>3. Elegibilidad</h2>
<p>Para utilizar los Servicios, debes:</p>
<ul>
    <li>Tener al menos 18 años de edad (o la mayoría de edad en tu jurisdicción, lo que sea mayor);</li>
    <li>Tener la capacidad legal para celebrar contratos vinculantes bajo las leyes de tu jurisdicción;</li>
    <li>No tener prohibido el uso de los Servicios bajo la ley aplicable; y</li>
    <li>Aceptar y cumplir con estos Términos.</li>
</ul>
<p>Los Servicios de Castle están diseñados para mujeres adultas que desean desarrollar su educación financiera y riqueza. Sin embargo, los Servicios están disponibles para todos los adultos que cumplan con los requisitos de elegibilidad anteriores. Al utilizar los Servicios, declaras y garantizas que cumples con todos los requisitos anteriores. Si no cumples con estos requisitos, no debes acceder ni utilizar los Servicios.</p>

<h2>4. Descripción de los Servicios</h2>
<p>Castle proporciona un Ecosistema Financiero de Inteligencia Artificial diseñado para ayudar a las mujeres a transformar su relación con el dinero y construir riqueza. Los Servicios actualmente incluyen, y pueden expandirse en el futuro para incluir, lo siguiente:</p>

<h3>4.1 Lista de espera y Comunidad</h3>
<p>Castle opera una lista de espera para usuarios potenciales que desean ser de los primeros en acceder a la plataforma. Al unirte a la lista de espera, nos proporcionas información de contacto y aceptas recibir actualizaciones y anuncios sobre la plataforma Castle.</p>

<h3>4.2 Serie de MasterClasses</h3>
<p>Castle ofrece una serie de MasterClasses en vivo centradas en la educación financiera, la mentalidad de riqueza y las estrategias de inversión. La participación en la MasterClass es únicamente por solicitud, sujeta a disponibilidad, y sujeta a los términos del programa separados comunicados a los solicitantes aceptados. La Serie de MasterClasses se ofrece actualmente de forma gratuita, aunque esto podría cambiar en el futuro. Castle se reserva el derecho de modificar, suspender o discontinuar cualquier programa de MasterClass en cualquier momento.</p>

<h3>4.3 Coach de Dinero y Riqueza de IA</h3>
<p>La plataforma de Castle incorpora un Coach de Dinero y Riqueza impulsado por IA que brinda orientación financiera personalizada, contenido educativo y herramientas de seguimiento de objetivos. Al interactuar con el Coach de IA, reconoces que el Coach de IA proporciona información únicamente con fines educativos e informativos; el contenido generado por IA no constituye asesoramiento financiero, de inversión, legal, fiscal o profesional; no debes confiar únicamente en el contenido generado por IA al tomar decisiones financieras; y los resultados de la IA pueden no ser precisos, completos o apropiados para tus circunstancias específicas.</p>

<h3>4.4 Integración de cuentas (Característica futura)</h3>
<p>Castle planea ofrecer características de integración de cuentas que te permitan conectar cuentas financieras externas (como cuentas bancarias, cuentas de corretaje u otras plataformas financieras) para ver y analizar tu situación financiera en un solo lugar. Cuando esta característica esté disponible, se aplicarán términos y divulgaciones adicionales.</p>

<h3>4.5 Marketplace de Inversiones (Característica futura)</h3>
<p>Castle planea ofrecer un Marketplace de Inversiones donde se puedan presentar oportunidades de inversión seleccionadas a los usuarios elegibles. Cuando y si el Marketplace de Inversiones esté disponible, estará sujeto a términos, condiciones y divulgaciones regulatorias independientes. La participación en el Marketplace de Inversiones requerirá tu reconocimiento de las divulgaciones de riesgo específicas y los requisitos de elegibilidad aplicables.</p>

<h3>4.6 Programa de Socios</h3>
<p>Castle ofrece un Programa de Socios para influencers, creadores de contenido, marcas, organizaciones de mujeres y expertos que deseen colaborar con Castle. La participación en el Programa de Socios está sujeta a un Acuerdo de Socio independiente y a los términos relacionados comunicados durante el proceso de solicitud e incorporación.</p>

<h3>4.7 Boletín y Comunicaciones</h3>
<p>Con tu consentimiento, Castle envía boletines, actualizaciones de la plataforma, notificaciones de eventos y otras comunicaciones. Puedes cancelar la suscripción a las comunicaciones de marketing en cualquier momento haciendo clic en el enlace 'darse de baja' en cualquier correo electrónico o poniéndote en contacto con nosotros en <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a>.</p>

<h2>5. Registro de Usuarios y Cuentas</h2>
<p>Para acceder a ciertas características de los Servicios, es posible que se te solicite crear una cuenta o enviar información de registro a través de nuestros formularios. Cuando te registras o envías información, aceptas: proporcionar información precisa, actual y completa; mantener y actualizar de inmediato tu información; mantener la seguridad y confidencialidad de cualquier credencial de cuenta; notificarnos inmediatamente sobre cualquier uso no autorizado de tu cuenta en <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a>; y aceptar la responsabilidad de todas las actividades que ocurran bajo tu cuenta.</p>
<p>Castle se reserva el derecho de suspender o rescindir tu cuenta si se determina que alguna información proporcionada es inexacta, falsa, desactualizada o incompleta, o si violas estos Términos.</p>

<h2>6. Conducta del Usuario</h2>
<p>Al utilizar los Servicios, aceptas no: utilizar los Servicios para cualquier propósito ilegal; suplantar a cualquier persona o entidad; publicar o transmitir contenido difamatorio, obsceno, ofensivo, amenazante o acosador; realizar conductas que restrinjan el uso de los Servicios; utilizar medios automatizados para acceder a los Servicios; intentar ganar acceso no autorizado a nuestros sistemas; transmitir virus o código malicioso; interferir en el rendimiento de los Servicios; enviar correos no deseados (spam); violar derechos de propiedad intelectual; o realizar manipulación del mercado o actividad financiera fraudulenta.</p>

<h2>7. Sin Asesoramiento Financiero — Descargo de Responsabilidad Importante</h2>
<p><strong>IMPORTANTE: CASTLE NO ES UN ASESOR DE INVERSIONES REGISTRADO, AGENTE DE BOLSA, PLANIFICADOR FINANCIERO, ANALISTA FINANCIERO O FIDUCIARIO. NADA EN LA PLATAFORMA CASTLE — INCLUYENDO EL COACH DE RIQUEZA DE IA, EL CONTENIDO EDUCATIVO, LA SERIE DE MASTERCLASSES, LOS BOLETINES, LA COMUNICACIONES DE SOCIOS O CUALQUIER OTRO SERVICIO — CONSTITUYE ASESORAMIENTO FINANCIERO, DE INVERSIÓN, FISCAL, LEGAL O PROFESIONAL DE NINGÚN TIPO.</strong></p>
<p>Todo el contenido, herramientas, materiales educativos y resultados generados por IA proporcionados a través de los Servicios son solo para fines informativos y educativos generales. No constituyen ni deben considerarse un sustituto del asesoramiento profesional financiero, de inversión, fiscal, legal u otro asesoramiento adaptado a tus circunstancias individuales.</p>
<p>Antes de tomar cualquier decisión financiera o de inversión, debes consultar a un asesor financiero calificado, asesor de inversiones, profesional de impuestos, abogado u otro profesional con licencia que pueda evaluar tu situación específica, tolerancia al riesgo y objetivos.</p>
<p>Castle no realiza ninguna declaración ni garantía sobre la idoneidad de ninguna oportunidad de inversión, estrategia financiera o curso de acción para ningún usuario en particular. El rendimiento pasado de cualquier inversión discutida o referenciada en la plataforma no es indicativo de resultados futuros. Todas las inversiones implican riesgos, incluida la posible pérdida del capital.</p>

<h2>8. Propiedad Intelectual</h2>
<h3>8.1 Propiedad Intelectual de Castle</h3>
<p>Todo el contenido, materiales, características y funcionalidad de los Servicios — incluyendo texto, gráficos, logotipos, iconos, imágenes, clips de audio y video, el nombre y marca de Castle, y la apariencia general — son propiedad de Build Your Castle, Inc. o de sus licenciantes y están protegidos por las leyes de derechos de autor, marcas comerciales, patentes, secretos comerciales y otras leyes de propiedad intelectual de los Estados Unidos e internacionales.</p>
<p>No puedes copiar, reproducir, distribuir, modificar o transmitir ningún contenido de los Servicios sin nuestro consentimiento previo por escrito, excepto para uso personal, no comercial y transitorio.</p>

<h3>8.2 Contenido Generado por el Usuario</h3>
<p>Si envías, publicas o trasmitas cualquier contenido a través de los Servicios, otorgas a Castle una licencia no exclusiva, mundial, libre de regalías, perpetua e irrevocable para usar, reproducir, modificar, adaptar, publicar y mostrar dicho contenido en relación con la operación y mejora de los Servicios, sujeto a nuestra Política de Privacidad.</p>

<h3>8.3 Comentarios</h3>
<p>Si proporcionas a Castle comentarios, sugerencias o ideas con respecto a los Servicios, otorgas a Castle una licencia ilimitada y libre de regalías para utilizar e incorporar dichos comentarios sin ninguna obligación para contigo.</p>

<h2>9. Características y Contenido de Inteligencia Artificial</h2>
<p>La plataforma de Castle incorpora tecnologías de inteligencia artificial. Reconoces y aceptas que los resultados generados por IA se producen de forma algorítmica y pueden no ser siempre precisos; Castle no garantiza la exactitud del contenido de IA; asumes la responsabilidad exclusiva de las decisiones tomadas sobre la base de la IA; Castle puede utilizar tus interacciones para mejorar los servicios bajo la Política de Privacidad; y las características de IA pueden ser modificadas o discontinuadas en cualquier momento.</p>

<h2>10. Características de Web3, Blockchain y Token Castle</h2>
<p>Castle está desarrollando un ecosistema impulsado por Web3 que incluye tokens basados en blockchain ("Tokens Castle"). Al participar, reconoces y aceptas que:</p>
<p><strong>LOS TOKENS CASTLE NO SON VALORES, PRODUCTOS DE INVERSIÓN NI INSTRUMENTOS FINANCIEROS. NO SE OFRECEN NI SE VENDEN COMO INVERSIONES Y NO OTORGAN NINGÚN INTERÉS DE PROPIEDAD, DERECHOS A DIVIDENDOS, DERECHOS DE VOTO U OTROS DERECHOS FINANCIEROS EN BUILD YOUR CASTLE, INC. O CUALQUIER ENTIDAD AFILIADA.</strong></p>
<p>Las transacciones en blockchain son irreversibles e inmutables. El valor de los tokens puede disminuir a cero. Eres responsable de cumplir con las leyes de tu jurisdicción. Castle se reserva el derecho de modificar o discontinuar el token, y los contratos inteligentes se proporcionan 'tal cual'.</p>

<h2>11. Enlaces, Contenido y Servicios de Terceros</h2>
<p>Los Servicios pueden contener enlaces o integrarse con sitios web o servicios de terceros (por ejemplo, redes sociales, Fundación Unicoin, plataformas de inversión). No controlamos ni asumimos responsabilidad por el contenido de terceros, y Castle no será responsable por pérdidas o daños en relación con ellos.</p>

<h2>12. Descargo de Responsabilidad de Garantías</h2>
<p><strong>LOS SERVICIOS SE PROPORCIONAN 'TAL CUAL' Y 'SEGÚN DISPONIBILIDAD', SIN NINGUNA GARANTÍA DE NINGÚN TIPO, YA SEA EXPRESA O IMPLÍCITA. EN LA MEDIDA MÁXIMA PERMITIDA POR LA LEY APLICABLE, CASTLE RECHAZA EXPRESAMENTE TODAS LAS GARANTÍAS, INCLUYENDO GARANTÍAS IMPLÍCITAS DE COMERCIABILIDAD, ADECUACIÓN PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN.</strong></p>

<h2>13. Limitación de Responsabilidad</h2>
<p><strong>EN LA MEDIDA MÁXIMA PERMITIDA POR LA LEY APLICABLE, EN NINGÚN CASO CASTLE, SUS AFILIADOS, OFICIALES O DIRECTORES SERÁN RESPONSABLES POR DAÑOS INDIRECTOS, INCIDENTALES, ESPECIALES, CONSECUENTES O PUNITIVOS, INCLUYENDO PÉRDIDA DE GANANCIAS, DATOS O USO.</strong></p>
<p><strong>LA RESPONSABILIDAD ACUMULADA TOTAL DE CASTLE NO EXCEDERÁ LA CANTIDAD QUE HAYA PAGADO A CASTLE EN LOS DOCE MESES ANTERIORES O CIEN DÓLARES ESTADOUNIDENSES (USD $100).</strong></p>

<h2>14. Indemnización</h2>
<p>Aceptas defender, indemnizar y eximir de responsabilidad a Build Your Castle, Inc., sus afiliados, oficiales y empleados de y contra cualquier reclamo, responsabilidad, daño, pérdida y gasto (incluyendo honorarios de abogados) que surjan de o se relacionen con tu uso de los Servicios, tu violación de estos Términos o tu violación de los derechos de terceros.</p>

<h2>15. Ley Aplicable y Resolución de Disputas</h2>
<h3>15.1 Ley Aplicable</h3>
<p>Estos Términos se rigen y se interpretan de acuerdo con las leyes del Estado de Delaware, Estados Unidos de América, sin tener en cuenta sus principios de conflicto de leyes.</p>

<h3>15.2 Resolución Informal</h3>
<p>Antes de iniciar acciones legales, aceptas contactar primero a Castle en <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a> para intentar resolver la disputa informalmente durante 30 días.</p>

<h3>15.3 Arbitraje</h3>
<p>Cualquier disputa no resuelta se resolverá mediante arbitraje vinculante administrado por la Asociación Americana de Arbitraje (AAA) bajo sus Reglas de Arbitraje del Consumidor, conducido en inglés.</p>

<h3>15.4 Renuncia a Demandas Colectivas</h3>
<p><strong>TÚ Y CASTLE ACUERDAN QUE CADA PARTE PUEDE PRESENTAR RECLAMACIONES CONTRA LA OTRA SOLO EN SU CAPACIDAD INDIVIDUAL Y NO COMO DEMANDANTE O MIEMBRO DE UNA CLASE EN NINGUNA SUPUESTA ACCIÓN COLECTIVA O REPRESENTATIVA.</strong></p>

<h2>16. Plazo y Rescisión</h2>
<p>Estos Términos permanecen vigentes hasta su rescisión. Castle puede suspender tu acceso en cualquier momento. Al terminar, tu derecho a usar los Servicios cesa de inmediato.</p>

<h2>17. Modificaciones a los Servicios</h2>
<p>Castle se reserva el derecho de modificar o discontinuar cualquier aspecto de los Servicios en cualquier momento sin previo aviso ni responsabilidad.</p>

<h2>18. Disposiciones Generales</h2>
<p>Estos Términos, la Política de Privacidad y la Política de Cookies constituyen el acuerdo completo. Si alguna disposición es inválida, las demás continúan en vigor. No puedes ceder estos Términos, pero Castle puede hacerlo libremente. Estos Términos están escritos en inglés, y cualquier traducción es para conveniencia únicamente.</p>

<h2>19. Contacto</h2>
<p>Si tienes alguna pregunta, inquietud o comentario sobre estos Términos, ponte en contacto con nosotros:</p>
<p class="contact-details">
    <strong>Build Your Castle, Inc.</strong><br>
    Attn: Legal Team<br>
    Email: <a href="mailto:legal@buildyourcastle.ai">legal@buildyourcastle.ai</a><br>
    Website: <a href="https://buildyourcastle.ai">buildyourcastle.ai</a>
</p>
"""

# HTML template with placeholder text replacements
# No f-strings, just standard replace
html_template = """<!DOCTYPE html>
<html lang="[LANG]">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[META_TITLE]</title>
    <!-- Open Graph / Social Media Meta Tags -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://natalia-unicoin.github.io/castle/">
    <meta property="og:title" content="[META_TITLE]">
    <meta property="og:description" content="The AI-powered platform helping Women build Wealth, invest with confidence, and earn rewards for financial progress.">
    <meta property="og:image" content="https://natalia-unicoin.github.io/castle/public/images/common/hero-bg.png?v=5">
    
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="https://natalia-unicoin.github.io/castle/">
    <meta name="twitter:title" content="[META_TITLE]">
    <meta name="twitter:description" content="The AI-powered platform helping Women build Wealth, invest with confidence, and earn rewards for financial progress.">
    <meta name="twitter:image" content="https://natalia-unicoin.github.io/castle/public/images/common/hero-bg.png?v=5">

    <link rel="icon" href="./public/images/common/favicon.png?v=10" type="image/png">
    <link rel="shortcut icon" href="./public/images/common/favicon.png?v=10">
    <link rel="apple-touch-icon" href="./public/images/common/favicon.png?v=10">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Caveat&family=Inter:wght@400;500;600;700;800;900&family=DM+Sans:wght@400;500;600;700;800;900&display=swap');
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { 
            font-family: 'Inter', system-ui, sans-serif; 
            background-color: #FFFFFF;
            color: #1A1A1A;
            overflow-x: hidden;
            line-height: 1.6;
        }
        
        /* Header */
        header {
            position: fixed; top: 0; left: 0; width: 100%; padding: 16px clamp(30px, 5vw, 100px);
            display: flex; justify-content: space-between; align-items: center;
            background: rgba(255, 255, 255, 0.98); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
            z-index: 100; border-bottom: 1px solid #E5E7EB; box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        }
        .header-logo img { height: 32px; width: auto; object-fit: contain; transition: transform 0.3s; }
        .header-logo:hover img { transform: scale(1.05); }
        
        .nav-links { display: flex; align-items: center; gap: 40px; }
        .nav-links a { color: #1A1A1A; text-decoration: none; font-size: 15px; font-weight: 600; font-family: 'Inter', sans-serif; transition: color 0.2s;  letter-spacing: 1px; }
        .nav-links a:hover { color: #A03FA3; }
        
        .header-actions { display: flex; align-items: center; gap: 24px; }
        .lang-select { 
            background-color: transparent; border: 1px solid #E5E7EB; font-family: 'Inter', sans-serif;
            background-repeat: no-repeat; background-position: right 4px center; background-size: 16px;
            -webkit-appearance: none; appearance: none;
            font-weight: 700; font-size: 14px; color: #1A1A1A !important; cursor: pointer; outline: none; padding: 4px 24px 4px 8px; border-radius: 4px;
        }
        .lang-select option { color: #1A1A1A; }
        .btn-nav {
            background: rgba(17,17,17,0.05); color: #1A1A1A; border: 1px solid rgba(17,17,17,0.1);
            padding: 10px 24px; border-radius: 5px; font-size: 12px; font-weight: 600; 
            text-decoration: none; transition: all 0.3s; font-family: 'Inter', sans-serif;
            letter-spacing: 1px; white-space: nowrap; 
        }
        .btn-nav:hover { background: #1A1A1A; color: #FFFFFF; border-color: #1A1A1A; }

        @media(max-width: 768px){
            .desktop-only { display: none !important; }
        }

        /* Legal Content */
        .legal-container {
            max-width: 900px;
            margin: 120px auto 80px auto;
            padding: 0 24px;
        }
        .legal-container h1 {
            font-size: clamp(32px, 5vw, 48px);
            font-weight: 800;
            color: #1A1A1A;
            margin-bottom: 8px;
            letter-spacing: -1px;
            line-height: 1.2;
        }
        .legal-container h2 {
            font-size: 24px;
            font-weight: 700;
            color: #A03FA3;
            margin-top: 40px;
            margin-bottom: 16px;
            border-bottom: 1px solid #F3F4F6;
            padding-bottom: 8px;
        }
        .legal-container h3 {
            font-size: 18px;
            font-weight: 700;
            color: #1A1A1A;
            margin-top: 24px;
            margin-bottom: 12px;
        }
        .legal-container p {
            font-size: 16px;
            color: #374151;
            margin-bottom: 16px;
            line-height: 1.6;
        }
        .legal-container ul {
            margin-left: 24px;
            margin-bottom: 20px;
            color: #374151;
        }
        .legal-container li {
            margin-bottom: 8px;
            font-size: 16px;
        }
        .legal-container a {
            color: #A03FA3;
            text-decoration: none;
            font-weight: 600;
        }
        .legal-container a:hover {
            text-decoration: underline;
        }
        .last-updated {
            font-size: 14px;
            color: #6B7280 !important;
            margin-bottom: 40px;
            font-style: italic;
        }
        .contact-details {
            background: #F9FAFB;
            border-left: 4px solid #A03FA3;
            padding: 20px;
            border-radius: 0 8px 8px 0;
            font-size: 15px;
            color: #4B5563;
        }

        /* Table Styling */
        .legal-table {
            width: 100%;
            border-collapse: collapse;
            margin: 24px 0;
            font-size: 15px;
            text-align: left;
        }
        .legal-table th, .legal-table td {
            padding: 14px 16px;
            border: 1px solid #E5E7EB;
        }
        .legal-table th {
            background-color: #F9FAFB;
            font-weight: 700;
            color: #1A1A1A;
        }
        .legal-table td code {
            background-color: #F3F4F6;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
            font-size: 14px;
        }
        @media(max-width: 600px){
            .legal-table, .legal-table tbody, .legal-table tr, .legal-table td, .legal-table th {
                display: block;
                width: 100%;
            }
            .legal-table tr {
                margin-bottom: 15px;
                border: 1px solid #E5E7EB;
            }
            .legal-table td, .legal-table th {
                border: none;
                border-bottom: 1px solid #F3F4F6;
            }
            .legal-table th {
                display: none;
            }
            .legal-table td::before {
                content: attr(data-label);
                font-weight: 700;
                display: block;
                margin-bottom: 4px;
            }
        }

        /* Footer */
        .site-footer {
            background-color: #111111;
            color: #FFFFFF;
            padding: 80px 4vw 40px 4vw;
            font-family: 'Inter', sans-serif;
        }
        .site-footer .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        .footer-grid {
            display: grid;
            grid-template-columns: 2fr repeat(3, 1fr);
            gap: 40px;
            margin-bottom: 60px;
        }
        @media (max-width: 768px) {
            .footer-grid {
                grid-template-columns: 1fr;
                gap: 30px;
            }
        }
        .footer-logo {
            height: 32px;
            margin-bottom: 20px;
        }
        .footer-brand p {
            color: #9CA3AF;
            font-size: 15px;
            max-width: 250px;
            line-height: 1.5;
        }
        .footer-col h4 {
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 24px;
            color: #FFFFFF;
            letter-spacing: 1px;
            text-transform: uppercase;
        }
        .footer-col a {
            display: block;
            color: #9CA3AF;
            text-decoration: none;
            margin-bottom: 12px;
            font-size: 15px;
            transition: color 0.2s;
        }
        .footer-col a:hover {
            color: #FFFFFF;
        }
        .footer-bottom {
            border-top: 1px solid #1F2937;
            padding-top: 30px;
            text-align: center;
            font-size: 13px;
            color: #9CA3AF;
        }
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <a href="[LOGO_HREF]" class="header-logo">
            <img src="./public/images/common/logo-dark.png" alt="Castle Logo">
        </a>
        <nav class="nav-links desktop-only">
            [NAV_LINKS]
        </nav>
        <div class="header-actions">
            [LANG_SELECT]
            <a href="index.html" class="btn-nav">[ENTER_APP_TEXT]</a>
        </div>
    </header>

    <!-- Main Content -->
    <main class="legal-container">
        [BODY_CONTENT]
    </main>

    <!-- Footer -->
    <footer class="site-footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col footer-brand">
                    <img src="./public/images/common/logo-light.png" alt="Castle Logo" class="footer-logo">
                    <p>[TAGLINE]</p>
                </div>
                <div class="footer-col">
                    <h4>[COL_COMPANY]</h4>
                    <a href="[LINK_ABOUT]">[LINK_ABOUT_TEXT]</a>
                    <a href="[LINK_PARTNERS]">[LINK_PARTNERS_TEXT]</a>
                    <a href="[LINK_CONTACT]">[LINK_CONTACT_TEXT]</a>
                </div>
                <div class="footer-col">
                    <h4>[COL_RESOURCES]</h4>
                    <a href="[LINK_MC]">Masterclass</a>
                </div>
                <div class="footer-col">
                    <h4>[COL_LEGAL]</h4>
                    <a href="privacy-policy.html">[LINK_PRIVACY_TEXT]</a>
                    <a href="terms-of-service.html">[LINK_TERMS_TEXT]</a>
                    <a href="cookie-policy.html">[LINK_COOKIES_TEXT]</a>
                </div>
            </div>
            
            <div style="text-align: center; font-size: 11px; color: #6B7280; margin-bottom: 15px;">
                [DISCLAIMER]
            </div>
            <div class="footer-bottom">
                &copy; 2026 Castle. All rights reserved.
            </div>
        </div>
    </footer>

</body>
</html>
"""

def generate_legal_html(filename, lang, title, body_content):
    is_spanish = (lang == "es")
    
    # Language switch URL
    if is_spanish:
        en_filename = filename.replace('_es.html', '.html')
        lang_select_html = '<select class="lang-select" onchange="location = this.value;" style="color: #1A1A1A !important; border-color: #E5E7EB; background-image: url(\'data:image/svg+xml;utf8,<svg fill=\\"%231A1A1A\\" height=\\"24\\" viewBox=\\"0 0 24 24\\" width=\\"24\\" xmlns=\\"http://www.w3.org/2000/svg\\"><path d=\\"M7 10l5 5 5-5z\\"/><path d=\\"M0 0h24v24H0z\\" fill=\\"none\\"/></svg>\');"><option value="' + en_filename + '">EN</option><option value="' + filename + '" selected>ES</option></select>'
        nav_html = """
            <a href="about_es.html">SOBRE NOSOTROS</a>
            <a href="partners_es.html">SOCIOS</a>
            <a href="masterclass_es.html">MASTERCLASS</a>
            <a href="contact_es.html">CONTACTO</a>
        """
        logo_href = "index_es.html"
        enter_app_text = "ENTRAR A LA APP"
        tagline = "Sé dueña de tu Dinero. Sé dueña de tu Futuro."
        col_company = "Compañía"
        col_resources = "Recursos"
        col_legal = "Legal"
        link_about = "about_es.html"
        link_about_text = "Sobre Nosotros"
        link_partners = "partners_es.html"
        link_partners_text = "Socios"
        link_contact = "contact_es.html"
        link_contact_text = "Contacto"
        link_mc = "masterclass_es.html"
        link_privacy_text = "Política de Privacidad"
        link_terms_text = "Términos de Servicio"
        link_cookies_text = "Política de Cookies"
        disclaimer = "Las imágenes utilizadas en este sitio fueron creadas o modificadas con IA y son solo para fines ilustrativos."
    else:
        es_filename = filename.replace('.html', '_es.html')
        lang_select_html = '<select class="lang-select" onchange="location = this.value;" style="color: #1A1A1A !important; border-color: #E5E7EB; background-image: url(\'data:image/svg+xml;utf8,<svg fill=\'#1A1A1A\' height=\'24\' viewBox=\'0 0 24 24\' width=\'24\' xmlns=\'http://www.w3.org/2000/svg\'><path d=\'M7 10l5 5 5-5z\'/><path d=\'M0 0h24v24H0z\' fill=\'none\'/></svg>\');"><option value="' + filename + '" selected>EN</option><option value="' + es_filename + '">ES</option></select>'
        nav_html = """
            <a href="about.html">ABOUT</a>
            <a href="partners.html">PARTNERS</a>
            <a href="masterclass.html">MASTERCLASS</a>
            <a href="contact.html">CONTACT</a>
        """
        logo_href = "index.html"
        enter_app_text = "ENTER APP"
        tagline = "Own Your Wealth. Own Your Future."
        col_company = "Company"
        col_resources = "Resources"
        col_legal = "Legal"
        link_about = "about.html"
        link_about_text = "About Us"
        link_partners = "partners.html"
        link_partners_text = "Partners"
        link_contact = "contact.html"
        link_contact_text = "Contact"
        link_mc = "masterclass.html"
        link_privacy_text = "Privacy Policy"
        link_terms_text = "Terms of Service"
        link_cookies_text = "Cookie Policy"
        disclaimer = "The images used on this site were created or modified with AI and are for illustrative purposes only."

    meta_title = "Castle | " + tagline

    content = html_template
    content = content.replace("[LANG]", lang)
    content = content.replace("[META_TITLE]", meta_title)
    content = content.replace("[LOGO_HREF]", logo_href)
    content = content.replace("[NAV_LINKS]", nav_html)
    content = content.replace("[LANG_SELECT]", lang_select_html)
    content = content.replace("[ENTER_APP_TEXT]", enter_app_text)
    content = content.replace("[BODY_CONTENT]", body_content)
    content = content.replace("[TAGLINE]", tagline)
    content = content.replace("[COL_COMPANY]", col_company)
    content = content.replace("[LINK_ABOUT]", link_about)
    content = content.replace("[LINK_ABOUT_TEXT]", link_about_text)
    content = content.replace("[LINK_PARTNERS]", link_partners)
    content = content.replace("[LINK_PARTNERS_TEXT]", link_partners_text)
    content = content.replace("[LINK_CONTACT]", link_contact)
    content = content.replace("[LINK_CONTACT_TEXT]", link_contact_text)
    content = content.replace("[COL_RESOURCES]", col_resources)
    content = content.replace("[LINK_MC]", link_mc)
    content = content.replace("[COL_LEGAL]", col_legal)
    content = content.replace("[LINK_PRIVACY_TEXT]", link_privacy_text)
    content = content.replace("[LINK_TERMS_TEXT]", link_terms_text)
    content = content.replace("[LINK_COOKIES_TEXT]", link_cookies_text)
    content = content.replace("[DISCLAIMER]", disclaimer)

    # For Spanish pages, adjust privacy/terms links to ES versions
    if is_spanish:
        content = content.replace('href="privacy-policy.html"', 'href="privacy-policy_es.html"')
        content = content.replace('href="terms-of-service.html"', 'href="terms-of-service_es.html"')
        content = content.replace('href="cookie-policy.html"', 'href="cookie-policy_es.html"')

    return content

# Write Cookie Policy files
with open("cookie-policy.html", "w", encoding="utf-8") as f:
    f.write(generate_legal_html("cookie-policy.html", "en", "Cookie Policy", cookie_policy_en))

with open("cookie-policy_es.html", "w", encoding="utf-8") as f:
    f.write(generate_legal_html("cookie-policy_es.html", "es", "Política de Cookies", cookie_policy_es))

# Write Privacy Policy files
with open("privacy-policy.html", "w", encoding="utf-8") as f:
    f.write(generate_legal_html("privacy-policy.html", "en", "Privacy Policy", privacy_policy_en))

with open("privacy-policy_es.html", "w", encoding="utf-8") as f:
    f.write(generate_legal_html("privacy-policy_es.html", "es", "Política de Privacidad", privacy_policy_es))

# Write Terms of Use files
with open("terms-of-service.html", "w", encoding="utf-8") as f:
    f.write(generate_legal_html("terms-of-service.html", "en", "Terms of Service", terms_of_use_en))

with open("terms-of-service_es.html", "w", encoding="utf-8") as f:
    f.write(generate_legal_html("terms-of-service_es.html", "es", "Términos de Servicio", terms_of_use_es))

print("Created legal pages successfully!")

# Update footer links in all active HTML files
html_files = [
    "index.html",
    "index_es.html",
    "about.html",
    "about_es.html",
    "contact.html",
    "contact_es.html",
    "partners.html",
    "partners_es.html",
    "masterclass.html",
    "masterclass_es.html",
    "masterclass_v2.html",
    "masterclass_v2_es.html",
    "thank-you.html",
    "gracias.html"
]

for filename in html_files:
    if not os.path.exists(filename):
        continue
        
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace Cookie Policy links
    content = re.sub(
        r'<a\s+href=["\']#["\']>\s*Cookie\s+Policy\s*</a>',
        '<a href="cookie-policy.html">Cookie Policy</a>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<a\s+href=["\']#["\']>\s*Pol&iacute;tica\s+de\s+Cookies\s*</a>',
        '<a href="cookie-policy_es.html">Política de Cookies</a>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<a\s+href=["\']#["\']>\s*Pol&iacute;tica\s+de\s+cookies\s*</a>',
        '<a href="cookie-policy_es.html">Política de Cookies</a>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<a\s+href=["\']#["\']>\s*Política\s+de\s+Cookies\s*</a>',
        '<a href="cookie-policy_es.html">Política de Cookies</a>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<a\s+href=["\']#["\']>\s*Política\s+de\s+cookies\s*</a>',
        '<a href="cookie-policy_es.html">Política de Cookies</a>',
        content,
        flags=re.IGNORECASE
    )

    # Replace Privacy Policy links
    content = re.sub(
        r'<a\s+href=["\']#["\']>\s*Privacy\s+Policy\s*</a>',
        '<a href="privacy-policy.html">Privacy Policy</a>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<a\s+href=["\']#["\']>\s*Pol&iacute;tica\s+de\s+Privacidad\s*</a>',
        '<a href="privacy-policy_es.html">Política de Privacidad</a>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<a\s+href=["\']#["\']>\s*Pol&iacute;tica\s+de\s+privacidad\s*</a>',
        '<a href="privacy-policy_es.html">Política de Privacidad</a>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<a\s+href=["\']#["\']>\s*Política\s+de\s+Privacidad\s*</a>',
        '<a href="privacy-policy_es.html">Política de Privacidad</a>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<a\s+href=["\']#["\']>\s*Política\s+de\s+privacidad\s*</a>',
        '<a href="privacy-policy_es.html">Política de Privacidad</a>',
        content,
        flags=re.IGNORECASE
    )

    # Replace Terms of Use / Terms of Service links
    content = re.sub(
        r'<a\s+href=["\']#["\']>\s*Terms\s+of\s+Service\s*</a>',
        '<a href="terms-of-service.html">Terms of Service</a>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<a\s+href=["\']#["\']>\s*T&eacute;rminos\s+de\s+Servicio\s*</a>',
        '<a href="terms-of-service_es.html">Términos de Servicio</a>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<a\s+href=["\']#["\']>\s*T&eacute;rminos\s+de\s+servicio\s*</a>',
        '<a href="terms-of-service_es.html">Términos de Servicio</a>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<a\s+href=["\']#["\']>\s*Términos\s+de\s+Servicio\s*</a>',
        '<a href="terms-of-service_es.html">Términos de Servicio</a>',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<a\s+href=["\']#["\']>\s*Términos\s+de\s+servicio\s*</a>',
        '<a href="terms-of-service_es.html">Términos de Servicio</a>',
        content,
        flags=re.IGNORECASE
    )

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Updated footer links in {filename}")

print("All tasks completed successfully!")
