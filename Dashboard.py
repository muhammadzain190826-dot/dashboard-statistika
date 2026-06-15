<?xml version='1.0' encoding='utf-8' ?>

<!-- build 20261.26.0512.1636                               -->
<workbook original-version='18.1' source-build='2026.1.2 (20261.26.0512.1636)' source-platform='mac' version='18.1' xmlns:user='http://www.tableausoftware.com/xml/user'>
  <document-format-change-manifest>
    <AccessibleZoneTabOrder />
    <AnimationOnByDefault />
    <AutoCreateAndUpdateDSDPhoneLayouts />
    <_.fcp.DashboardRoundedCorners.true...DashboardRoundedCorners />
    <IntuitiveSorting />
    <IntuitiveSorting_SP2 />
    <MarkAnimation />
    <ObjectModelEncapsulateLegacy />
    <ObjectModelTableType />
    <ParameterAction />
    <ParameterActionClearSelection />
    <SchemaViewerObjectModel />
    <SetMembershipControl />
    <SheetIdentifierTracking />
    <SortTagCleanup />
    <WindowsPersistSimpleIdentifiers />
    <WorksheetBackgroundTransparency />
  </document-format-change-manifest>
  <preferences>
    <preference name='ui.encoding.shelf.height' value='24' />
    <preference name='ui.shelf.height' value='26' />
  </preferences>
  <datasources>
    <datasource hasconnection='false' inline='true' name='Parameters' version='18.1'>
      <aliases enabled='yes' />
      <column caption='ColorCenter 1' datatype='real' name='[ColorCenter 1]' param-domain-type='any' role='measure' type='quantitative' value='7.0'>
        <calculation class='tableau' formula='7.0' />
      </column>
      <column caption='ColorCenter' datatype='integer' name='[ColorCenter]' param-domain-type='any' role='measure' type='quantitative' value='8'>
        <calculation class='tableau' formula='8' />
      </column>
    </datasource>
    <datasource caption='Sheet1 (Data_Kebiasaan_Belajar_Tableau)' inline='true' name='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm' version='18.1'>
      <connection class='federated'>
        <named-connections>
          <named-connection caption='Data_Kebiasaan_Belajar_Tableau' name='excel-direct.18fbxn013m93xz1d0m3qn1ofjy4c'>
            <connection class='excel-direct' cleaning='no' compat='no' dataRefreshTime='' filename='/Volumes/ZAIN/Analisis Data/Data_Kebiasaan_Belajar_Tableau.xlsx' interpretationMode='0' password='' server='' validate='no' />
          </named-connection>
        </named-connections>
        <relation connection='excel-direct.18fbxn013m93xz1d0m3qn1ofjy4c' name='Sheet1' table='[Sheet1$]' type='table'>
          <columns gridOrigin='A1:AA31:no:A1:AA31:0' header='yes' outcome='6'>
            <column datatype='integer' name='No' ordinal='0' />
            <column datatype='string' name='Nama' ordinal='1' />
            <column datatype='integer' name='Semester' ordinal='2' />
            <column datatype='string' name='Jenis Kelamin' ordinal='3' />
            <column datatype='string' name='Rentang IPK' ordinal='4' />
            <column datatype='string' name='Jam Belajar per Hari' ordinal='5' />
            <column datatype='string' name='Waktu Belajar Favorit' ordinal='6' />
            <column datatype='string' name='Frekuensi Belajar' ordinal='7' />
            <column datatype='string' name='Tempat Belajar' ordinal='8' />
            <column datatype='integer' name='Tingkat Distraksi' ordinal='9' />
            <column datatype='string' name='Mulai Belajar Ujian' ordinal='10' />
            <column datatype='string' name='Jam Belajar Ujian' ordinal='11' />
            <column datatype='integer' name='Skor Kepuasan' ordinal='12' />
            <column datatype='string' name='Persepsi Korelasi Nilai' ordinal='13' />
            <column datatype='integer' name='Metode: Baca Catatan' ordinal='14' />
            <column datatype='integer' name='Metode: Rangkuman/MindMap' ordinal='15' />
            <column datatype='integer' name='Metode: Soal Latihan' ordinal='16' />
            <column datatype='integer' name='Metode: Belajar Kelompok' ordinal='17' />
            <column datatype='integer' name='Metode: Video' ordinal='18' />
            <column datatype='integer' name='Metode: AI Tools' ordinal='19' />
            <column datatype='integer' name='Metode: Flashcard' ordinal='20' />
            <column datatype='integer' name='Hambatan: Susah Fokus' ordinal='21' />
            <column datatype='integer' name='Hambatan: Kelelahan' ordinal='22' />
            <column datatype='integer' name='Hambatan: Tdk Tahu Metode' ordinal='23' />
            <column datatype='integer' name='Hambatan: Banyak Tugas' ordinal='24' />
            <column datatype='integer' name='Hambatan: Kurang Motivasi' ordinal='25' />
            <column datatype='integer' name='Hambatan: Lingkungan' ordinal='26' />
          </columns>
        </relation>
        <metadata-records>
          <metadata-record class='capability'>
            <remote-name />
            <remote-type>0</remote-type>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias />
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='integer' name='context'>0</attribute>
              <attribute datatype='string' name='gridOrigin'>&quot;A1:AA31:no:A1:AA31:0&quot;</attribute>
              <attribute datatype='boolean' name='header'>true</attribute>
              <attribute datatype='integer' name='outcome'>6</attribute>
            </attributes>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>No</remote-name>
            <remote-type>20</remote-type>
            <local-name>[No]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>No</remote-alias>
            <ordinal>0</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Nama</remote-name>
            <remote-type>130</remote-type>
            <local-name>[Nama]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Nama</remote-alias>
            <ordinal>1</ordinal>
            <local-type>string</local-type>
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
            <collation flag='1' name='LEN_RID_S2' />
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;WSTR&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Semester</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Semester]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Semester</remote-alias>
            <ordinal>2</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Jenis Kelamin</remote-name>
            <remote-type>130</remote-type>
            <local-name>[Jenis Kelamin]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Jenis Kelamin</remote-alias>
            <ordinal>3</ordinal>
            <local-type>string</local-type>
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
            <collation flag='1' name='LEN_RID_S2' />
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;WSTR&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Rentang IPK</remote-name>
            <remote-type>130</remote-type>
            <local-name>[Rentang IPK]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Rentang IPK</remote-alias>
            <ordinal>4</ordinal>
            <local-type>string</local-type>
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
            <collation flag='1' name='LEN_RID_S2' />
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;WSTR&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Jam Belajar per Hari</remote-name>
            <remote-type>130</remote-type>
            <local-name>[Jam Belajar per Hari]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Jam Belajar per Hari</remote-alias>
            <ordinal>5</ordinal>
            <local-type>string</local-type>
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
            <collation flag='1' name='LEN_RID_S2' />
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;WSTR&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Waktu Belajar Favorit</remote-name>
            <remote-type>130</remote-type>
            <local-name>[Waktu Belajar Favorit]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Waktu Belajar Favorit</remote-alias>
            <ordinal>6</ordinal>
            <local-type>string</local-type>
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
            <collation flag='1' name='LEN_RID_S2' />
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;WSTR&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Frekuensi Belajar</remote-name>
            <remote-type>130</remote-type>
            <local-name>[Frekuensi Belajar]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Frekuensi Belajar</remote-alias>
            <ordinal>7</ordinal>
            <local-type>string</local-type>
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
            <collation flag='1' name='LEN_RID_S2' />
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;WSTR&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Tempat Belajar</remote-name>
            <remote-type>130</remote-type>
            <local-name>[Tempat Belajar]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Tempat Belajar</remote-alias>
            <ordinal>8</ordinal>
            <local-type>string</local-type>
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
            <collation flag='1' name='LEN_RID_S2' />
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;WSTR&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Tingkat Distraksi</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Tingkat Distraksi]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Tingkat Distraksi</remote-alias>
            <ordinal>9</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Mulai Belajar Ujian</remote-name>
            <remote-type>130</remote-type>
            <local-name>[Mulai Belajar Ujian]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Mulai Belajar Ujian</remote-alias>
            <ordinal>10</ordinal>
            <local-type>string</local-type>
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
            <collation flag='1' name='LEN_RID_S2' />
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;WSTR&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Jam Belajar Ujian</remote-name>
            <remote-type>130</remote-type>
            <local-name>[Jam Belajar Ujian]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Jam Belajar Ujian</remote-alias>
            <ordinal>11</ordinal>
            <local-type>string</local-type>
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
            <collation flag='1' name='LEN_RID_S2' />
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;WSTR&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Skor Kepuasan</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Skor Kepuasan]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Skor Kepuasan</remote-alias>
            <ordinal>12</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Persepsi Korelasi Nilai</remote-name>
            <remote-type>130</remote-type>
            <local-name>[Persepsi Korelasi Nilai]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Persepsi Korelasi Nilai</remote-alias>
            <ordinal>13</ordinal>
            <local-type>string</local-type>
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
            <collation flag='1' name='LEN_RID_S2' />
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;WSTR&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Metode: Baca Catatan</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Metode: Baca Catatan]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Metode: Baca Catatan</remote-alias>
            <ordinal>14</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Metode: Rangkuman/MindMap</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Metode: Rangkuman/MindMap]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Metode: Rangkuman/MindMap</remote-alias>
            <ordinal>15</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Metode: Soal Latihan</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Metode: Soal Latihan]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Metode: Soal Latihan</remote-alias>
            <ordinal>16</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Metode: Belajar Kelompok</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Metode: Belajar Kelompok]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Metode: Belajar Kelompok</remote-alias>
            <ordinal>17</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Metode: Video</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Metode: Video]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Metode: Video</remote-alias>
            <ordinal>18</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Metode: AI Tools</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Metode: AI Tools]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Metode: AI Tools</remote-alias>
            <ordinal>19</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Metode: Flashcard</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Metode: Flashcard]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Metode: Flashcard</remote-alias>
            <ordinal>20</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Hambatan: Susah Fokus</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Hambatan: Susah Fokus]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Hambatan: Susah Fokus</remote-alias>
            <ordinal>21</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Hambatan: Kelelahan</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Hambatan: Kelelahan]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Hambatan: Kelelahan</remote-alias>
            <ordinal>22</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Hambatan: Tdk Tahu Metode</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Hambatan: Tdk Tahu Metode]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Hambatan: Tdk Tahu Metode</remote-alias>
            <ordinal>23</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Hambatan: Banyak Tugas</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Hambatan: Banyak Tugas]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Hambatan: Banyak Tugas</remote-alias>
            <ordinal>24</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Hambatan: Kurang Motivasi</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Hambatan: Kurang Motivasi]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Hambatan: Kurang Motivasi</remote-alias>
            <ordinal>25</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Hambatan: Lingkungan</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Hambatan: Lingkungan]</local-name>
            <parent-name>[Sheet1]</parent-name>
            <remote-alias>Hambatan: Lingkungan</remote-alias>
            <ordinal>26</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <attributes>
              <attribute datatype='string' name='DebugRemoteType'>&quot;I8&quot;</attribute>
            </attributes>
            <object-id>[Sheet1_B50A4972F6424C73AD3216E4765423B2]</object-id>
          </metadata-record>
        </metadata-records>
      </connection>
      <aliases enabled='yes' />
      <column datatype='string' name='[Frekuensi Belajar]' role='dimension' type='nominal' />
      <column datatype='integer' name='[Hambatan: Banyak Tugas]' role='measure' type='quantitative' />
      <column datatype='string' name='[Jam Belajar per Hari]' role='dimension' type='nominal' />
      <column datatype='string' name='[Jenis Kelamin]' role='dimension' type='nominal' />
      <column aggregation='None' datatype='integer' name='[No (bin)]' role='dimension' type='quantitative'>
        <calculation class='bin' decimals='0' formula='[No]' peg='0' size='2.83' />
      </column>
      <column datatype='integer' name='[No]' role='measure' type='quantitative' />
      <column datatype='string' name='[Rentang IPK]' role='dimension' type='nominal' />
      <column datatype='integer' name='[Skor Kepuasan]' role='measure' type='quantitative' />
      <column datatype='string' name='[Tempat Belajar]' role='dimension' type='nominal' />
      <column datatype='integer' name='[Tingkat Distraksi]' role='measure' type='quantitative' />
      <column datatype='string' name='[Waktu Belajar Favorit]' role='dimension' type='nominal' />
      <column caption='Sheet1' datatype='table' name='[__tableau_internal_object_id__].[Sheet1_B50A4972F6424C73AD3216E4765423B2]' role='measure' type='quantitative' />
      <column-instance column='[Frekuensi Belajar]' derivation='Count' name='[cnt:Frekuensi Belajar:qk]' pivot='key' type='quantitative' />
      <column-instance column='[Jam Belajar per Hari]' derivation='Count' name='[cnt:Jam Belajar per Hari:qk]' pivot='key' type='quantitative' />
      <column-instance column='[No]' derivation='Count' name='[cnt:No:qk]' pivot='key' type='quantitative' />
      <column-instance column='[Frekuensi Belajar]' derivation='None' name='[none:Frekuensi Belajar:nk]' pivot='key' type='nominal' />
      <column-instance column='[Jam Belajar per Hari]' derivation='None' name='[none:Jam Belajar per Hari:nk]' pivot='key' type='nominal' />
      <column-instance column='[Jenis Kelamin]' derivation='None' name='[none:Jenis Kelamin:nk]' pivot='key' type='nominal' />
      <column-instance column='[Rentang IPK]' derivation='None' name='[none:Rentang IPK:nk]' pivot='key' type='nominal' />
      <column-instance column='[Tempat Belajar]' derivation='None' name='[none:Tempat Belajar:nk]' pivot='key' type='nominal' />
      <column-instance column='[Waktu Belajar Favorit]' derivation='None' name='[none:Waktu Belajar Favorit:nk]' pivot='key' type='nominal' />
      <column-instance column='[Hambatan: Banyak Tugas]' derivation='Sum' name='[sum:Hambatan: Banyak Tugas:qk]' pivot='key' type='quantitative' />
      <column-instance column='[Skor Kepuasan]' derivation='Sum' name='[sum:Skor Kepuasan:qk]' pivot='key' type='quantitative' />
      <column-instance column='[Tingkat Distraksi]' derivation='Sum' name='[sum:Tingkat Distraksi:qk]' pivot='key' type='quantitative' />
      <group caption='Action (Jenis Kelamin)' hidden='true' name='[Action (Jenis Kelamin)]' name-style='unqualified' user:auto-column='sheet_link'>
        <groupfilter function='crossjoin'>
          <groupfilter function='level-members' level='[Jenis Kelamin]' />
        </groupfilter>
      </group>
      <group caption='Action (Rentang IPK)' hidden='true' name='[Action (Rentang IPK)]' name-style='unqualified' user:auto-column='sheet_link'>
        <groupfilter function='crossjoin'>
          <groupfilter function='level-members' level='[Rentang IPK]' />
        </groupfilter>
      </group>
      <group caption='Action (Tempat Belajar)' hidden='true' name='[Action (Tempat Belajar)]' name-style='unqualified' user:auto-column='sheet_link'>
        <groupfilter function='crossjoin'>
          <groupfilter function='level-members' level='[Tempat Belajar]' />
        </groupfilter>
      </group>
      <layout dim-ordering='alphabetic' measure-ordering='alphabetic' show-aliased-fields='true' show-structure='true' />
      <style>
        <style-rule element='mark'>
          <encoding attr='color' field='[none:Jenis Kelamin:nk]' palette='orange_gold_10_0' type='palette'>
            <map to='#9e3a26'>
              <bucket>&quot;Perempuan&quot;</bucket>
            </map>
            <map to='#f4d166'>
              <bucket>&quot;Laki-laki&quot;</bucket>
            </map>
          </encoding>
          <encoding attr='color' field='[none:Frekuensi Belajar:nk]' type='palette'>
            <map to='#4e79a7'>
              <bucket>&quot;Jarang&quot;</bucket>
            </map>
            <map to='#59a14f'>
              <bucket>&quot;Tidak Pernah&quot;</bucket>
            </map>
            <map to='#76b7b2'>
              <bucket>&quot;Setiap Hari&quot;</bucket>
            </map>
            <map to='#e15759'>
              <bucket>&quot;Sering&quot;</bucket>
            </map>
            <map to='#f28e2b'>
              <bucket>&quot;Kadang-kadang&quot;</bucket>
            </map>
          </encoding>
          <encoding attr='color' field='[none:Jam Belajar per Hari:nk]' type='palette'>
            <map to='#4e79a7'>
              <bucket>&quot;1-2 jam&quot;</bucket>
            </map>
            <map to='#76b7b2'>
              <bucket>&quot;&gt;4 jam&quot;</bucket>
            </map>
            <map to='#e15759'>
              <bucket>&quot;&lt;1 jam&quot;</bucket>
            </map>
            <map to='#f28e2b'>
              <bucket>&quot;3-4 jam&quot;</bucket>
            </map>
          </encoding>
          <encoding attr='color' field='[none:Waktu Belajar Favorit:nk]' palette='red_gold_10_0' type='palette'>
            <map to='#b71d3e'>
              <bucket>&quot;Sore&quot;</bucket>
            </map>
            <map to='#de5747'>
              <bucket>&quot;Pagi&quot;</bucket>
            </map>
            <map to='#f4d166'>
              <bucket>&quot;Dini Hari&quot;</bucket>
            </map>
            <map to='#fa8f4d'>
              <bucket>&quot;Malam&quot;</bucket>
            </map>
          </encoding>
          <encoding attr='color' field='[none:Tempat Belajar:nk]' palette='red_10_0' type='palette'>
            <map to='#ae123a'>
              <bucket>&quot;Kos/Rumah&quot;</bucket>
            </map>
            <map to='#ffbeb2'>
              <bucket>&quot;Bervariasi&quot;</bucket>
            </map>
          </encoding>
          <encoding attr='color' field='[:Measure Names]' type='palette'>
            <map to='#4e79a7'>
              <bucket>&quot;[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:Jam Belajar per Hari:qk]&quot;</bucket>
            </map>
            <map to='#59a14f'>
              <bucket>&quot;[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Hambatan: Banyak Tugas:qk]&quot;</bucket>
            </map>
            <map to='#76b7b2'>
              <bucket>&quot;[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Tingkat Distraksi:qk]&quot;</bucket>
            </map>
            <map to='#b07aa1'>
              <bucket>&quot;[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm]&quot;</bucket>
            </map>
            <map to='#e15759'>
              <bucket>&quot;[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Skor Kepuasan:qk]&quot;</bucket>
            </map>
            <map to='#edc948'>
              <bucket>&quot;[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:Frekuensi Belajar:qk]&quot;</bucket>
            </map>
            <map to='#f28e2b'>
              <bucket>&quot;[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]&quot;</bucket>
            </map>
            <map to='#f28e2b'>
              <bucket>&quot;[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Tempat Belajar:nk]&quot;</bucket>
            </map>
          </encoding>
          <encoding attr='color' field='[none:Rentang IPK:nk]' palette='red_gold_10_0' type='palette'>
            <map to='#b71d3e'>
              <bucket>&quot;3.50-4.00&quot;</bucket>
            </map>
            <map to='#f4d166'>
              <bucket>&quot;3.00-3.49&quot;</bucket>
            </map>
          </encoding>
        </style-rule>
      </style>
      <semantic-values>
        <semantic-value key='[Country].[Name]' value='&quot;Indonesia&quot;' />
      </semantic-values>
      <object-graph>
        <objects>
          <object caption='Sheet1' id='Sheet1_B50A4972F6424C73AD3216E4765423B2'>
            <properties context=''>
              <relation connection='excel-direct.18fbxn013m93xz1d0m3qn1ofjy4c' name='Sheet1' table='[Sheet1$]' type='table'>
                <columns gridOrigin='A1:AA31:no:A1:AA31:0' header='yes' outcome='6'>
                  <column datatype='integer' name='No' ordinal='0' />
                  <column datatype='string' name='Nama' ordinal='1' />
                  <column datatype='integer' name='Semester' ordinal='2' />
                  <column datatype='string' name='Jenis Kelamin' ordinal='3' />
                  <column datatype='string' name='Rentang IPK' ordinal='4' />
                  <column datatype='string' name='Jam Belajar per Hari' ordinal='5' />
                  <column datatype='string' name='Waktu Belajar Favorit' ordinal='6' />
                  <column datatype='string' name='Frekuensi Belajar' ordinal='7' />
                  <column datatype='string' name='Tempat Belajar' ordinal='8' />
                  <column datatype='integer' name='Tingkat Distraksi' ordinal='9' />
                  <column datatype='string' name='Mulai Belajar Ujian' ordinal='10' />
                  <column datatype='string' name='Jam Belajar Ujian' ordinal='11' />
                  <column datatype='integer' name='Skor Kepuasan' ordinal='12' />
                  <column datatype='string' name='Persepsi Korelasi Nilai' ordinal='13' />
                  <column datatype='integer' name='Metode: Baca Catatan' ordinal='14' />
                  <column datatype='integer' name='Metode: Rangkuman/MindMap' ordinal='15' />
                  <column datatype='integer' name='Metode: Soal Latihan' ordinal='16' />
                  <column datatype='integer' name='Metode: Belajar Kelompok' ordinal='17' />
                  <column datatype='integer' name='Metode: Video' ordinal='18' />
                  <column datatype='integer' name='Metode: AI Tools' ordinal='19' />
                  <column datatype='integer' name='Metode: Flashcard' ordinal='20' />
                  <column datatype='integer' name='Hambatan: Susah Fokus' ordinal='21' />
                  <column datatype='integer' name='Hambatan: Kelelahan' ordinal='22' />
                  <column datatype='integer' name='Hambatan: Tdk Tahu Metode' ordinal='23' />
                  <column datatype='integer' name='Hambatan: Banyak Tugas' ordinal='24' />
                  <column datatype='integer' name='Hambatan: Kurang Motivasi' ordinal='25' />
                  <column datatype='integer' name='Hambatan: Lingkungan' ordinal='26' />
                </columns>
              </relation>
            </properties>
          </object>
        </objects>
      </object-graph>
    </datasource>
  </datasources>
  <actions>
    <action caption='Filter 2 (generated)' name='[Action4_0EA4B52E834A4D468B6370BBEF73EC91]'>
      <activation auto-clear='true' type='on-select' />
      <source dashboard='Main Dashboard' type='sheet' worksheet='Tempat Belajar' />
      <command command='tsc:tsl-filter'>
        <param name='special-fields' value='all' />
        <param name='target' value='Main Dashboard' />
      </command>
    </action>
    <edit-parameter-action caption='ParameterColorCenter1' name='[Action1_7B30F4139F9647FD9153C8954F522F97]'>
      <activation type='on-select' />
      <source type='sheet' worksheet='jam belajar perhari' />
      <agg-type type='median' />
      <clear-option type='do-nothing' value='i:1' />
      <params>
        <param name='source-field' value='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:Jam Belajar per Hari:qk]' />
        <param name='target-parameter' value='[Parameters].[ColorCenter]' />
      </params>
    </edit-parameter-action>
    <edit-parameter-action caption='ParameterColorCenter2' name='[Action2_320F381E93C84F3D8DA36DD9D7F4B409]'>
      <activation type='on-select' />
      <source type='sheet' worksheet='Metode Belajar' />
      <agg-type type='median' />
      <clear-option type='do-nothing' value='i:1' />
      <params>
        <param name='source-field' value='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Multiple Values]' />
        <param name='target-parameter' value='[Parameters].[ColorCenter 1]' />
      </params>
    </edit-parameter-action>
  </actions>
  <worksheets>
    <worksheet name='Demografi 1'>
      <layout-options>
        <title>
          <formatted-text>
            <run bold='true' fontalignment='1' fontcolor='#f28e2b' fontsize='10'>Jenis Kelamin</run>
          </formatted-text>
        </title>
      </layout-options>
      <table>
        <view>
          <datasources>
            <datasource caption='Sheet1 (Data_Kebiasaan_Belajar_Tableau)' name='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm' />
          </datasources>
          <datasource-dependencies datasource='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm'>
            <column datatype='string' name='[Jenis Kelamin]' role='dimension' type='nominal' />
            <column datatype='integer' name='[No]' role='measure' type='quantitative' />
            <column datatype='string' name='[Tempat Belajar]' role='dimension' type='nominal' />
            <column-instance column='[No]' derivation='Count' name='[cnt:No:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Jenis Kelamin]' derivation='None' name='[none:Jenis Kelamin:nk]' pivot='key' type='nominal' />
          </datasource-dependencies>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]'>
            <groupfilter function='level-members' level='[Tempat Belajar]' user:ui-action-filter='[Action4_0EA4B52E834A4D468B6370BBEF73EC91]' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
          <slices>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]</column>
          </slices>
          <aggregation value='true' />
        </view>
        <style>
          <style-rule element='cell'>
            <format attr='color' value='#f28e2b' />
            <format attr='width' value='59' />
          </style-rule>
          <style-rule element='legend-title-text'>
            <format attr='color' field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Jenis Kelamin:nk]' value='Jenis Kelamin'>
              <formatted-text>
                <run>Jenis Kelamin</run>
              </formatted-text>
            </format>
          </style-rule>
        </style>
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Circle' />
            <mark-sizing mark-sizing-setting='marks-scaling-off' />
            <encodings>
              <color column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Jenis Kelamin:nk]' />
              <lod column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]' />
            </encodings>
            <style>
              <style-rule element='mark'>
                <format attr='mark-labels-show' value='true' />
                <format attr='mark-color' value='#f28e2b' />
                <format attr='size' value='1.4612706899642944' />
              </style-rule>
              <style-rule element='pane'>
                <format attr='minwidth' value='-1' />
                <format attr='maxwidth' value='-1' />
              </style-rule>
            </style>
          </pane>
        </panes>
        <rows>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Jenis Kelamin:nk]</rows>
        <cols />
      </table>
      <simple-id uuid='{D9C4E63B-4F44-4774-A347-F4D1066DE6F4}' />
    </worksheet>
    <worksheet name='IPK Distribution'>
      <layout-options>
        <title>
          <formatted-text>
            <run fontalignment='1' fontcolor='#e15759' fontsize='10'>&lt;Sheet Name&gt;</run>
          </formatted-text>
        </title>
      </layout-options>
      <table>
        <view>
          <datasources>
            <datasource caption='Sheet1 (Data_Kebiasaan_Belajar_Tableau)' name='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm' />
          </datasources>
          <datasource-dependencies datasource='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm'>
            <column datatype='string' name='[Jenis Kelamin]' role='dimension' type='nominal' />
            <column datatype='integer' name='[No]' role='measure' type='quantitative' />
            <column datatype='string' name='[Rentang IPK]' role='dimension' type='nominal' />
            <column datatype='string' name='[Tempat Belajar]' role='dimension' type='nominal' />
            <column-instance column='[No]' derivation='Count' name='[cnt:No:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Rentang IPK]' derivation='None' name='[none:Rentang IPK:nk]' pivot='key' type='nominal' />
          </datasource-dependencies>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Jenis Kelamin)]'>
            <groupfilter function='member' level='[Jenis Kelamin]' member='&quot;Perempuan&quot;' user:ui-action-filter='[Action1_9E1BD9363C224602AF40AAF3285FBBB3]' user:ui-domain='database' user:ui-enumeration='inclusive' user:ui-marker='enumerate' />
          </filter>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]'>
            <groupfilter function='level-members' level='[Tempat Belajar]' user:ui-action-filter='[Action4_0EA4B52E834A4D468B6370BBEF73EC91]' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
          <shelf-sorts>
            <shelf-sort-v2 dimension-to-sort='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Rentang IPK:nk]' direction='DESC' is-on-innermost-dimension='true' measure-to-sort-by='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]' shelf='rows' />
          </shelf-sorts>
          <slices>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Jenis Kelamin)]</column>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]</column>
          </slices>
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Line' />
            <encodings>
              <color column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Rentang IPK:nk]' />
            </encodings>
            <style>
              <style-rule element='mark'>
                <format attr='mark-labels-show' value='true' />
                <format attr='mark-labels-cull' value='true' />
                <format attr='mark-color' value='#9f39d9' />
              </style-rule>
            </style>
          </pane>
        </panes>
        <rows>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Rentang IPK:nk]</rows>
        <cols>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]</cols>
      </table>
      <simple-id uuid='{4AE1019A-1565-4FD3-9E04-C9E46F884942}' />
    </worksheet>
    <worksheet name='KPI Cards'>
      <layout-options>
        <title>
          <formatted-text>
            <run bold='true' fontcolor='#f28e2b'>&lt;Sheet Name&gt;</run>
          </formatted-text>
        </title>
      </layout-options>
      <table>
        <view>
          <datasources>
            <datasource caption='Sheet1 (Data_Kebiasaan_Belajar_Tableau)' name='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm' />
          </datasources>
          <datasource-dependencies datasource='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm'>
            <column datatype='string' name='[Jenis Kelamin]' role='dimension' type='nominal' />
            <column datatype='integer' name='[Skor Kepuasan]' role='measure' type='quantitative' />
            <column datatype='string' name='[Tempat Belajar]' role='dimension' type='nominal' />
            <column-instance column='[Skor Kepuasan]' derivation='Avg' name='[avg:Skor Kepuasan:qk]' pivot='key' type='quantitative' />
          </datasource-dependencies>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Jenis Kelamin)]'>
            <groupfilter function='level-members' level='[Jenis Kelamin]' user:ui-action-filter='[Action1_9E1BD9363C224602AF40AAF3285FBBB3]' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]'>
            <groupfilter function='level-members' level='[Tempat Belajar]' user:ui-action-filter='[Action4_0EA4B52E834A4D468B6370BBEF73EC91]' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
          <slices>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Jenis Kelamin)]</column>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]</column>
          </slices>
          <aggregation value='true' />
        </view>
        <style>
          <style-rule element='cell'>
            <format attr='height' value='43' />
          </style-rule>
        </style>
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Automatic' />
            <mark-sizing mark-sizing-setting='marks-scaling-off' />
            <encodings>
              <text column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[avg:Skor Kepuasan:qk]' />
            </encodings>
            <customized-label>
              <formatted-text>
                <run bold='true' fontsize='24'>&lt;</run>
                <run bold='true' fontsize='24'>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[avg:Skor Kepuasan:qk]</run>
                <run bold='true' fontsize='24'>&gt;</run>
              </formatted-text>
            </customized-label>
            <style>
              <style-rule element='mark'>
                <format attr='mark-labels-show' value='true' />
                <format attr='mark-labels-cull' value='true' />
                <format attr='size' value='2.1546962261199951' />
              </style-rule>
              <style-rule element='pane'>
                <format attr='minheight' value='-1' />
                <format attr='maxheight' value='-1' />
              </style-rule>
            </style>
          </pane>
        </panes>
        <rows />
        <cols />
      </table>
      <simple-id uuid='{639D79E4-4D87-4C78-A84F-F71E8CE22075}' />
    </worksheet>
    <worksheet name='Korelasi Tingkat Distraksi vs Skor Kepuasan'>
      <layout-options>
        <title>
          <formatted-text>
            <run fontalignment='1' fontcolor='#000000' fontname='Benton Sans Book' fontsize='10'>Hubungan Tingkat Distraksi vs Kepuasan</run>
          </formatted-text>
        </title>
      </layout-options>
      <table>
        <view>
          <datasources>
            <datasource caption='Sheet1 (Data_Kebiasaan_Belajar_Tableau)' name='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm' />
          </datasources>
          <datasource-dependencies datasource='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm'>
            <column datatype='string' name='[Jenis Kelamin]' role='dimension' type='nominal' />
            <column datatype='integer' name='[Skor Kepuasan]' role='measure' type='quantitative' />
            <column datatype='string' name='[Tempat Belajar]' role='dimension' type='nominal' />
            <column datatype='integer' name='[Tingkat Distraksi]' role='measure' type='quantitative' />
            <column-instance column='[Skor Kepuasan]' derivation='Sum' name='[sum:Skor Kepuasan:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Tingkat Distraksi]' derivation='Sum' name='[sum:Tingkat Distraksi:qk]' pivot='key' type='quantitative' />
          </datasource-dependencies>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Jenis Kelamin)]'>
            <groupfilter function='level-members' level='[Jenis Kelamin]' user:ui-action-filter='[Action1_9E1BD9363C224602AF40AAF3285FBBB3]' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]'>
            <groupfilter function='level-members' level='[Tempat Belajar]' user:ui-action-filter='[Action4_0EA4B52E834A4D468B6370BBEF73EC91]' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
          <slices>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Jenis Kelamin)]</column>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]</column>
          </slices>
          <aggregation value='false' />
        </view>
        <style>
          <style-rule element='mark'>
            <encoding attr='color' field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Skor Kepuasan:qk]' max='5' min='2' num-steps='5' palette='red_10_0' type='interpolated' />
            <encoding attr='color' field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Tingkat Distraksi:qk]' palette='sunrise_sunset_diverging_10_0' type='interpolated' />
          </style-rule>
        </style>
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Automatic' />
            <mark-sizing mark-sizing-setting='marks-scaling-off' />
            <encodings>
              <color column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Tingkat Distraksi:qk]' />
            </encodings>
            <style>
              <style-rule element='mark'>
                <format attr='size' value='1.1094474792480469' />
                <format attr='shape' value=':filled/circle' />
              </style-rule>
            </style>
          </pane>
        </panes>
        <rows>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Skor Kepuasan:qk]</rows>
        <cols>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Tingkat Distraksi:qk]</cols>
      </table>
      <simple-id uuid='{48B3AE9B-FF5C-4E1D-BCC2-B99D36C28777}' />
    </worksheet>
    <worksheet name='Metode Belajar'>
      <layout-options>
        <title>
          <formatted-text>
            <run bold='true' fontalignment='1' fontcolor='#000000'>&lt;Sheet Name&gt;</run>
          </formatted-text>
        </title>
      </layout-options>
      <table>
        <view>
          <datasources>
            <datasource caption='Sheet1 (Data_Kebiasaan_Belajar_Tableau)' name='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm' />
          </datasources>
          <datasource-dependencies datasource='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm'>
            <column datatype='string' name='[Jenis Kelamin]' role='dimension' type='nominal' />
            <column datatype='integer' name='[Metode: AI Tools]' role='measure' type='quantitative' />
            <column datatype='integer' name='[Metode: Baca Catatan]' role='measure' type='quantitative' />
            <column datatype='integer' name='[Metode: Belajar Kelompok]' role='measure' type='quantitative' />
            <column datatype='integer' name='[Metode: Flashcard]' role='measure' type='quantitative' />
            <column datatype='integer' name='[Metode: Rangkuman/MindMap]' role='measure' type='quantitative' />
            <column datatype='integer' name='[Metode: Soal Latihan]' role='measure' type='quantitative' />
            <column datatype='integer' name='[Metode: Video]' role='measure' type='quantitative' />
            <column datatype='string' name='[Tempat Belajar]' role='dimension' type='nominal' />
            <column-instance column='[Metode: AI Tools]' derivation='Count' name='[cnt:Metode: AI Tools:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Metode: Baca Catatan]' derivation='Sum' name='[sum:Metode: Baca Catatan:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Metode: Belajar Kelompok]' derivation='Sum' name='[sum:Metode: Belajar Kelompok:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Metode: Flashcard]' derivation='Sum' name='[sum:Metode: Flashcard:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Metode: Rangkuman/MindMap]' derivation='Sum' name='[sum:Metode: Rangkuman/MindMap:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Metode: Soal Latihan]' derivation='Sum' name='[sum:Metode: Soal Latihan:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Metode: Video]' derivation='Sum' name='[sum:Metode: Video:qk]' pivot='key' type='quantitative' />
          </datasource-dependencies>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[:Measure Names]'>
            <groupfilter function='union' user:op='manual'>
              <groupfilter function='member' level='[:Measure Names]' member='&quot;[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:Metode: AI Tools:qk]&quot;' />
              <groupfilter function='member' level='[:Measure Names]' member='&quot;[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Metode: Baca Catatan:qk]&quot;' />
              <groupfilter function='member' level='[:Measure Names]' member='&quot;[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Metode: Belajar Kelompok:qk]&quot;' />
              <groupfilter function='member' level='[:Measure Names]' member='&quot;[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Metode: Flashcard:qk]&quot;' />
              <groupfilter function='member' level='[:Measure Names]' member='&quot;[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Metode: Rangkuman/MindMap:qk]&quot;' />
              <groupfilter function='member' level='[:Measure Names]' member='&quot;[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Metode: Soal Latihan:qk]&quot;' />
              <groupfilter function='member' level='[:Measure Names]' member='&quot;[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Metode: Video:qk]&quot;' />
            </groupfilter>
          </filter>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Jenis Kelamin)]'>
            <groupfilter function='level-members' level='[Jenis Kelamin]' user:ui-action-filter='[Action1_9E1BD9363C224602AF40AAF3285FBBB3]' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]'>
            <groupfilter function='level-members' level='[Tempat Belajar]' user:ui-action-filter='[Action4_0EA4B52E834A4D468B6370BBEF73EC91]' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
          <slices>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Jenis Kelamin)]</column>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[:Measure Names]</column>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]</column>
          </slices>
          <aggregation value='true' />
        </view>
        <style>
          <style-rule element='field-labels'>
            <format attr='font-family' value='Tahoma' />
          </style-rule>
          <style-rule element='mark'>
            <encoding attr='color' field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Multiple Values]' num-steps='5' palette='red_gold_10_0' reverse='true' type='interpolated' />
          </style-rule>
        </style>
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Automatic' />
            <encodings>
              <color column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Multiple Values]' />
            </encodings>
          </pane>
        </panes>
        <rows>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[:Measure Names]</rows>
        <cols>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Multiple Values]</cols>
      </table>
      <simple-id uuid='{BC20C2AE-962E-49E1-8B92-BB636CB44D15}' />
    </worksheet>
    <worksheet name='Tempat Belajar'>
      <layout-options>
        <title>
          <formatted-text>
            <run bold='true' fontalignment='1' fontcolor='#e15759' fontsize='10'>&lt;Sheet Name&gt;</run>
          </formatted-text>
        </title>
      </layout-options>
      <table>
        <view>
          <datasources>
            <datasource caption='Sheet1 (Data_Kebiasaan_Belajar_Tableau)' name='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm' />
          </datasources>
          <datasource-dependencies datasource='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm'>
            <column datatype='string' name='[Jenis Kelamin]' role='dimension' type='nominal' />
            <column datatype='integer' name='[No]' role='measure' type='quantitative' />
            <column datatype='string' name='[Tempat Belajar]' role='dimension' type='nominal' />
            <column-instance column='[No]' derivation='Count' name='[cnt:No:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Tempat Belajar]' derivation='None' name='[none:Tempat Belajar:nk]' pivot='key' type='nominal' />
          </datasource-dependencies>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Jenis Kelamin)]'>
            <groupfilter function='level-members' level='[Jenis Kelamin]' user:ui-action-filter='[Action1_9E1BD9363C224602AF40AAF3285FBBB3]' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
          <shelf-sorts>
            <shelf-sort-v2 dimension-to-sort='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Tempat Belajar:nk]' direction='DESC' is-on-innermost-dimension='true' measure-to-sort-by='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]' shelf='rows' />
          </shelf-sorts>
          <slices>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Jenis Kelamin)]</column>
          </slices>
          <aggregation value='true' />
        </view>
        <style>
          <style-rule element='mark'>
            <encoding attr='size-bar' field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]' field-type='quantitative' max-size='1' min-size='0.005' type='centersize' />
          </style-rule>
        </style>
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Square' />
            <mark-sizing mark-sizing-setting='marks-scaling-off' />
            <encodings>
              <color column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Tempat Belajar:nk]' />
              <text column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]' />
            </encodings>
            <style>
              <style-rule element='mark'>
                <format attr='has-stroke' value='false' />
                <format attr='mark-labels-cull' value='true' />
                <format attr='mark-labels-line-first' value='true' />
                <format attr='mark-labels-line-last' value='true' />
                <format attr='mark-labels-range-min' value='true' />
                <format attr='mark-labels-range-max' value='true' />
                <format attr='mark-labels-mode' value='all' />
                <format attr='mark-labels-range-scope' value='pane' />
                <format attr='mark-labels-range-field' value='' />
                <format attr='size' value='1.7031491994857788' />
                <format attr='mark-labels-show' value='true' />
              </style-rule>
            </style>
          </pane>
        </panes>
        <rows>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Tempat Belajar:nk]</rows>
        <cols />
      </table>
      <simple-id uuid='{9F6EBEBE-3DDA-441F-AA25-4E082A0E00D7}' />
    </worksheet>
    <worksheet name='Waktu Belajar Favorit'>
      <layout-options>
        <title>
          <formatted-text>
            <run bold='true' fontalignment='1' fontcolor='#e15759' fontsize='10'>&lt;Sheet Name&gt;</run>
          </formatted-text>
        </title>
      </layout-options>
      <table>
        <view>
          <datasources>
            <datasource caption='Sheet1 (Data_Kebiasaan_Belajar_Tableau)' name='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm' />
          </datasources>
          <datasource-dependencies datasource='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm'>
            <column datatype='string' name='[Jenis Kelamin]' role='dimension' type='nominal' />
            <column datatype='integer' name='[No]' role='measure' type='quantitative' />
            <column datatype='string' name='[Tempat Belajar]' role='dimension' type='nominal' />
            <column datatype='string' name='[Waktu Belajar Favorit]' role='dimension' type='nominal' />
            <column-instance column='[No]' derivation='Count' name='[cnt:No:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Tempat Belajar]' derivation='None' name='[none:Tempat Belajar:nk]' pivot='key' type='nominal' />
            <column-instance column='[Waktu Belajar Favorit]' derivation='None' name='[none:Waktu Belajar Favorit:nk]' pivot='key' type='nominal' />
          </datasource-dependencies>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Jenis Kelamin)]'>
            <groupfilter function='level-members' level='[Jenis Kelamin]' user:ui-action-filter='[Action1_9E1BD9363C224602AF40AAF3285FBBB3]' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]'>
            <groupfilter function='level-members' level='[Tempat Belajar]' user:ui-action-filter='[Action4_0EA4B52E834A4D468B6370BBEF73EC91]' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
          <slices>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Jenis Kelamin)]</column>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]</column>
          </slices>
          <aggregation value='true' />
        </view>
        <style>
          <style-rule element='axis'>
            <format attr='height' field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]' value='59' />
          </style-rule>
          <style-rule element='cell'>
            <format attr='height' field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Waktu Belajar Favorit:nk]' value='19' />
          </style-rule>
          <style-rule element='legend-title-text'>
            <format attr='color' field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Tempat Belajar:nk]' value='Tempat Belajar'>
              <formatted-text>
                <run>Tempat Belajar</run>
              </formatted-text>
            </format>
          </style-rule>
        </style>
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Automatic' />
            <encodings>
              <color column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Tempat Belajar:nk]' />
            </encodings>
          </pane>
        </panes>
        <rows>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Waktu Belajar Favorit:nk]</rows>
        <cols>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]</cols>
      </table>
      <simple-id uuid='{D956F75B-0AE2-4058-94C4-617E6FB86A2C}' />
    </worksheet>
    <worksheet name='frekuensi'>
      <layout-options>
        <title>
          <formatted-text>
            <run bold='true' fontalignment='1' fontcolor='#f28e2b' fontsize='10'>Frekuensi belajar</run>
          </formatted-text>
        </title>
      </layout-options>
      <table>
        <view>
          <datasources>
            <datasource caption='Sheet1 (Data_Kebiasaan_Belajar_Tableau)' name='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm' />
          </datasources>
          <datasource-dependencies datasource='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm'>
            <column datatype='string' name='[Frekuensi Belajar]' role='dimension' type='nominal' />
            <column datatype='string' name='[Tempat Belajar]' role='dimension' type='nominal' />
            <column-instance column='[Frekuensi Belajar]' derivation='Count' name='[cnt:Frekuensi Belajar:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Frekuensi Belajar]' derivation='None' name='[none:Frekuensi Belajar:nk]' pivot='key' type='nominal' />
          </datasource-dependencies>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]'>
            <groupfilter function='level-members' level='[Tempat Belajar]' user:ui-action-filter='[Action4_0EA4B52E834A4D468B6370BBEF73EC91]' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
          <manual-sort column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Frekuensi Belajar:nk]' direction='ASC'>
            <dictionary>
              <bucket>&quot;Tidak Pernah&quot;</bucket>
              <bucket>&quot;Jarang&quot;</bucket>
              <bucket>&quot;Kadang-kadang&quot;</bucket>
              <bucket>&quot;Sering&quot;</bucket>
              <bucket>&quot;Setiap Hari&quot;</bucket>
            </dictionary>
          </manual-sort>
          <slices>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]</column>
          </slices>
          <aggregation value='true' />
        </view>
        <style>
          <style-rule element='cell'>
            <format attr='cell-w' value='20' />
            <format attr='cell-h' value='20' />
            <format attr='cell' value='20' />
            <format attr='cell-q' value='100' />
          </style-rule>
          <style-rule element='mark'>
            <encoding attr='color' field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:Frekuensi Belajar:qk]' palette='orange_blue_diverging_10_0' type='interpolated' />
            <encoding attr='size-bar' field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:Frekuensi Belajar:qk]' field-type='quantitative' max-size='1' min-size='0.005' type='centersize' />
          </style-rule>
        </style>
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Automatic' />
            <encodings>
              <color column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Frekuensi Belajar:nk]' />
              <size column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:Frekuensi Belajar:qk]' />
            </encodings>
            <style>
              <style-rule element='mark'>
                <format attr='size' value='1.7999999523162842' />
              </style-rule>
            </style>
          </pane>
        </panes>
        <rows>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Frekuensi Belajar:nk]</rows>
        <cols />
      </table>
      <simple-id uuid='{AC39CA2A-8C6D-4853-9942-5600DA4EF5F9}' />
    </worksheet>
    <worksheet name='jam belajar perhari'>
      <layout-options>
        <title>
          <formatted-text>
            <run bold='true' fontalignment='1' fontcolor='#f28e2b' fontname='Damascus' fontsize='11'>Jam Belajar Perhari</run>
          </formatted-text>
        </title>
      </layout-options>
      <table>
        <view>
          <datasources>
            <datasource caption='Sheet1 (Data_Kebiasaan_Belajar_Tableau)' name='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm' />
          </datasources>
          <datasource-dependencies datasource='federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm'>
            <column datatype='string' name='[Frekuensi Belajar]' role='dimension' type='nominal' />
            <column datatype='string' name='[Jam Belajar Ujian]' role='dimension' type='nominal' />
            <column datatype='string' name='[Jam Belajar per Hari]' role='dimension' type='nominal' />
            <column datatype='string' name='[Jenis Kelamin]' role='dimension' type='nominal' />
            <column datatype='integer' name='[No]' role='measure' type='quantitative' />
            <column datatype='string' name='[Tempat Belajar]' role='dimension' type='nominal' />
            <column-instance column='[Frekuensi Belajar]' derivation='Count' name='[cnt:Frekuensi Belajar:qk]' pivot='key' type='quantitative' />
            <column-instance column='[No]' derivation='Count' name='[cnt:No:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Jam Belajar Ujian]' derivation='None' name='[none:Jam Belajar Ujian:nk]' pivot='key' type='nominal' />
            <column-instance column='[Jam Belajar per Hari]' derivation='None' name='[none:Jam Belajar per Hari:nk]' pivot='key' type='nominal' />
          </datasource-dependencies>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Jenis Kelamin)]'>
            <groupfilter function='level-members' level='[Jenis Kelamin]' user:ui-action-filter='[Action1_9E1BD9363C224602AF40AAF3285FBBB3]' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
          <filter class='categorical' column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]'>
            <groupfilter function='level-members' level='[Tempat Belajar]' user:ui-action-filter='[Action4_0EA4B52E834A4D468B6370BBEF73EC91]' user:ui-enumeration='all' user:ui-marker='enumerate' />
          </filter>
          <slices>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Jenis Kelamin)]</column>
            <column>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Action (Tempat Belajar)]</column>
          </slices>
          <aggregation value='true' />
        </view>
        <style>
          <style-rule element='cell'>
            <format attr='border-style' scope='cols' value='solid' />
            <format attr='text-align' value='center' />
            <format attr='vertical-align' value='center' />
            <format attr='font-style' data-class='subtotal' scope='rows' value='normal' />
            <format attr='font-weight' data-class='subtotal' scope='rows' value='bold' />
            <format attr='font-weight' data-class='total' scope='rows' value='bold' />
            <format attr='font-style' data-class='total' scope='rows' value='normal' />
            <format attr='border-color' scope='cols' value='#f28e2b' />
            <format attr='font-size' field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]' value='8' />
          </style-rule>
          <style-rule element='header'>
            <format attr='band-color' scope='cols' value='#00000000' />
            <format attr='background-color' value='#00000000' />
            <format attr='band-color' scope='rows' value='#00000000' />
            <format attr='background-color' field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]' value='#ffffff' />
          </style-rule>
          <style-rule element='field-labels'>
            <format attr='background-color' value='#00000000' />
            <format attr='font-weight' value='normal' />
            <format attr='font-family' value='Zapf Dingbats' />
            <format attr='color' value='#f28e2b' />
            <format attr='font-size' value='8' />
          </style-rule>
          <style-rule element='field-labels-spanner'>
            <format attr='color' scope='cols' value='#f28e2b' />
          </style-rule>
          <style-rule element='label'>
            <format attr='font-family' scope='rows' value='Zapf Dingbats' />
            <format attr='font-style' scope='rows' value='normal' />
            <format attr='font-weight' scope='rows' value='bold' />
            <format attr='font-size' scope='rows' value='9' />
            <format attr='font-style' scope='cols' value='normal' />
          </style-rule>
          <style-rule element='pane'>
            <format attr='band-color' scope='cols' value='#00000000' />
            <format attr='background-color' value='#00000000' />
            <format attr='band-color' scope='rows' value='#00000000' />
          </style-rule>
          <style-rule element='table'>
            <format attr='band-size' scope='cols' value='3' />
            <format attr='background-color' value='#00000000' />
            <format attr='band-size' scope='rows' value='1' />
          </style-rule>
          <style-rule element='worksheet'>
            <format attr='color' value='#f28e2b' />
            <format attr='font-weight' value='bold' />
            <format attr='font-style' value='normal' />
          </style-rule>
          <style-rule element='refline'>
            <format attr='stroke-color' id='refline0' value='#000000' />
          </style-rule>
          <style-rule element='refboxplot'>
            <format attr='fill-color' id='refline0' value='#f0f0f0d9' />
            <format attr='palette' id='refline0' value='bp_orange' />
            <format attr='opacity' id='refline0' value='167' />
            <format attr='whisker-end' id='refline0' value='large' />
            <format attr='whisker-stroke-color' id='refline0' value='#f28e2b' />
            <format attr='whisker-stroke-size' id='refline0' value='2' />
            <format attr='stroke-color' id='refline0' value='#f28e2b' />
            <format attr='stroke-size' id='refline0' value='2' />
            <format attr='boxplot-style' id='refline0' value='modern' />
          </style-rule>
          <style-rule element='zeroline'>
            <format attr='line-visibility' value='on' />
            <format attr='line-pattern-only' value='dashed' />
            <format attr='stroke-color' value='#4e79a7' />
          </style-rule>
          <style-rule element='legend-title-text'>
            <format attr='color' field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Jam Belajar per Hari:nk]' value='Jam Belajar per Hari'>
              <formatted-text>
                <run>Jam Belajar per Hari</run>
              </formatted-text>
            </format>
          </style-rule>
        </style>
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Circle' />
            <encodings>
              <color column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Jam Belajar per Hari:nk]' />
              <lod column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:Frekuensi Belajar:qk]' />
            </encodings>
            <reference-line axis-column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]' boxplot-mark-exclusion='false' boxplot-whisker-type='standard' enable-instant-analytics='true' formula='average' id='refline0' label-type='automatic' probability='95' scope='per-cell' symmetric='false' value-column='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]' z-order='1' />
            <style>
              <style-rule element='mark'>
                <format attr='size' value='0.25' />
                <format attr='mark-color' value='#f28e2b' />
              </style-rule>
            </style>
          </pane>
        </panes>
        <rows>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]</rows>
        <cols>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Jam Belajar Ujian:nk]</cols>
      </table>
      <simple-id uuid='{74545AFC-E5C9-4DB5-81DA-0DB760EAEA3B}' />
    </worksheet>
  </worksheets>
  <dashboards>
    <dashboard enable-sort-zone-taborder='true' name='Main Dashboard'>
      <style />
      <size sizing-mode='automatic' />
      <zones>
        <zone h='100000' id='2' type-v2='layout-basic' w='100000' x='0' y='0'>
          <zone h='97922' id='32' param='horz' type-v2='layout-flow' w='98750' x='625' y='1039'>
            <zone h='97922' id='20' param='horz' type-v2='layout-flow' w='98750' x='625' y='1039'>
              <zone h='97922' id='16' param='horz' type-v2='layout-flow' w='77266' x='625' y='1039'>
                <zone h='97922' id='7' param='horz' type-v2='layout-flow' w='77266' x='625' y='1039'>
                  <zone h='97922' id='5' type-v2='layout-basic' w='77266' x='625' y='1039'>
                    <zone forceUpdate='true' h='25584' id='3' type-v2='text' w='26892' x='625' y='1039'>
                      <formatted-text>
                        <run fontcolor='#f28e2b' fontname='Marker Felt' fontsize='20' underline='true'>DASHBOARD ANALISIS BELAJAR MAHASISWA</run>
                      </formatted-text>
                      <zone-style>
                        <format attr='border-color' value='#000000' />
                        <format attr='border-style' value='none' />
                        <format attr='border-width' value='0' />
                        <format attr='margin' value='4' />
                      </zone-style>
                    </zone>
                    <zone h='25584' id='10' name='KPI Cards' w='27267' x='27517' y='1039'>
                      <zone-style>
                        <format attr='border-color' value='#000000' />
                        <format attr='border-style' value='none' />
                        <format attr='border-width' value='0' />
                        <format attr='margin' value='4' />
                      </zone-style>
                    </zone>
                    <zone h='27128' id='13' name='Korelasi Tingkat Distraksi vs Skor Kepuasan' w='38619' x='625' y='26623'>
                      <zone-style>
                        <format attr='border-color' value='#000000' />
                        <format attr='border-style' value='none' />
                        <format attr='border-width' value='0' />
                        <format attr='margin' value='4' />
                      </zone-style>
                    </zone>
                    <zone h='25584' id='14' name='Demografi 1' w='23107' x='54784' y='1039'>
                      <zone-style>
                        <format attr='border-color' value='#000000' />
                        <format attr='border-style' value='none' />
                        <format attr='border-width' value='0' />
                        <format attr='margin' value='4' />
                      </zone-style>
                    </zone>
                    <zone h='45210' id='24' name='Metode Belajar' w='49875' x='28016' y='53751'>
                      <layout-cache minwidth='180' type-h='cell' type-w='scalable' />
                      <zone-style>
                        <format attr='border-color' value='#000000' />
                        <format attr='border-style' value='none' />
                        <format attr='border-width' value='0' />
                        <format attr='margin' value='4' />
                      </zone-style>
                    </zone>
                    <zone h='23907' id='28' name='frekuensi' w='27391' x='625' y='75054'>
                      <zone-style>
                        <format attr='border-color' value='#000000' />
                        <format attr='border-style' value='none' />
                        <format attr='border-width' value='0' />
                        <_.fcp.DashboardRoundedCorners.true...format attr='corner-radius' value='7' />
                        <format attr='margin' value='4' />
                        <format attr='background-color' value='#ffb55734' />
                      </zone-style>
                    </zone>
                    <zone h='27128' id='11' name='IPK Distribution' w='38647' x='39244' y='26623'>
                      <zone-style>
                        <format attr='border-color' value='#000000' />
                        <format attr='border-style' value='none' />
                        <format attr='border-width' value='0' />
                        <format attr='margin' value='4' />
                      </zone-style>
                    </zone>
                    <zone h='21303' id='18' name='Tempat Belajar' w='27391' x='625' y='53751'>
                      <zone-style>
                        <format attr='border-color' value='#f28e2b' />
                        <format attr='border-style' value='solid' />
                        <format attr='border-width' value='1' />
                        <_.fcp.DashboardRoundedCorners.true...format attr='corner-radius' value='9' />
                        <format attr='margin' value='8' />
                        <format attr='background-color' value='#ff4f5a37' />
                      </zone-style>
                    </zone>
                  </zone>
                </zone>
              </zone>
              <zone fixed-size='275' h='97922' id='26' is-fixed='true' type-v2='layout-basic' w='21484' x='77891' y='1039'>
                <zone h='52712' id='30' name='jam belajar perhari' w='21484' x='77891' y='1039'>
                  <zone-style>
                    <format attr='border-color' value='#000000' />
                    <format attr='border-style' value='none' />
                    <format attr='border-width' value='0' />
                    <format attr='margin' value='4' />
                  </zone-style>
                </zone>
                <zone h='45210' id='22' name='Waktu Belajar Favorit' w='21484' x='77891' y='53751'>
                  <layout-cache fixed-size-h='188' type-h='fixed' type-w='fixed' />
                  <zone-style>
                    <format attr='border-color' value='#000000' />
                    <format attr='border-style' value='none' />
                    <format attr='border-width' value='0' />
                    <format attr='margin' value='4' />
                  </zone-style>
                </zone>
              </zone>
            </zone>
          </zone>
          <zone-style>
            <format attr='border-color' value='#000000' />
            <format attr='border-style' value='none' />
            <format attr='border-width' value='0' />
            <format attr='margin' value='8' />
          </zone-style>
        </zone>
      </zones>
      <devicelayouts>
        <devicelayout auto-generated='true' name='Phone'>
          <size maxheight='2150' minheight='2150' sizing-mode='vscroll' />
          <zones>
            <zone h='100000' id='38' type-v2='layout-basic' w='100000' x='0' y='0'>
              <zone h='97922' id='37' param='vert' type-v2='layout-flow' w='98750' x='625' y='1039'>
                <zone forceUpdate='true' h='25584' id='3' type-v2='text' w='26892' x='625' y='1039'>
                  <formatted-text>
                    <run fontcolor='#f28e2b' fontname='Marker Felt' fontsize='20' underline='true'>DASHBOARD ANALISIS BELAJAR MAHASISWA</run>
                  </formatted-text>
                  <zone-style>
                    <format attr='border-color' value='#000000' />
                    <format attr='border-style' value='none' />
                    <format attr='border-width' value='0' />
                    <format attr='margin' value='4' />
                    <format attr='padding' value='0' />
                  </zone-style>
                </zone>
                <zone fixed-size='197' h='25584' id='10' is-fixed='true' name='KPI Cards' w='27267' x='27517' y='1039'>
                  <zone-style>
                    <format attr='border-color' value='#000000' />
                    <format attr='border-style' value='none' />
                    <format attr='border-width' value='0' />
                    <format attr='margin' value='4' />
                    <format attr='padding' value='0' />
                  </zone-style>
                </zone>
                <zone fixed-size='197' h='25584' id='14' is-fixed='true' name='Demografi 1' w='23107' x='54784' y='1039'>
                  <zone-style>
                    <format attr='border-color' value='#000000' />
                    <format attr='border-style' value='none' />
                    <format attr='border-width' value='0' />
                    <format attr='margin' value='4' />
                    <format attr='padding' value='0' />
                  </zone-style>
                </zone>
                <zone fixed-size='280' h='52712' id='30' is-fixed='true' name='jam belajar perhari' w='21484' x='77891' y='1039'>
                  <zone-style>
                    <format attr='border-color' value='#000000' />
                    <format attr='border-style' value='none' />
                    <format attr='border-width' value='0' />
                    <format attr='margin' value='4' />
                    <format attr='padding' value='0' />
                  </zone-style>
                </zone>
                <zone fixed-size='209' h='27128' id='13' is-fixed='true' name='Korelasi Tingkat Distraksi vs Skor Kepuasan' w='38619' x='625' y='26623'>
                  <zone-style>
                    <format attr='border-color' value='#000000' />
                    <format attr='border-style' value='none' />
                    <format attr='border-width' value='0' />
                    <format attr='margin' value='4' />
                    <format attr='padding' value='0' />
                  </zone-style>
                </zone>
                <zone fixed-size='209' h='27128' id='11' is-fixed='true' name='IPK Distribution' w='38647' x='39244' y='26623'>
                  <zone-style>
                    <format attr='border-color' value='#000000' />
                    <format attr='border-style' value='none' />
                    <format attr='border-width' value='0' />
                    <format attr='margin' value='4' />
                    <format attr='padding' value='0' />
                  </zone-style>
                </zone>
                <zone fixed-size='152' h='21303' id='18' is-fixed='true' name='Tempat Belajar' w='27391' x='625' y='53751'>
                  <zone-style>
                    <format attr='border-color' value='#f28e2b' />
                    <format attr='border-style' value='solid' />
                    <format attr='border-width' value='1' />
                    <_.fcp.DashboardRoundedCorners.true...format attr='corner-radius' value='9' />
                    <format attr='margin' value='4' />
                    <format attr='padding' value='0' />
                    <format attr='background-color' value='#ff4f5a37' />
                  </zone-style>
                </zone>
                <zone fixed-size='280' h='45210' id='24' is-fixed='true' name='Metode Belajar' w='49875' x='28016' y='53751'>
                  <layout-cache minwidth='180' type-h='cell' type-w='scalable' />
                  <zone-style>
                    <format attr='border-color' value='#000000' />
                    <format attr='border-style' value='none' />
                    <format attr='border-width' value='0' />
                    <format attr='margin' value='4' />
                    <format attr='padding' value='0' />
                  </zone-style>
                </zone>
                <zone fixed-size='280' h='45210' id='22' is-fixed='true' name='Waktu Belajar Favorit' w='21484' x='77891' y='53751'>
                  <layout-cache fixed-size-h='188' type-h='fixed' type-w='fixed' />
                  <zone-style>
                    <format attr='border-color' value='#000000' />
                    <format attr='border-style' value='none' />
                    <format attr='border-width' value='0' />
                    <format attr='margin' value='4' />
                    <format attr='padding' value='0' />
                  </zone-style>
                </zone>
                <zone fixed-size='184' h='23907' id='28' is-fixed='true' name='frekuensi' w='27391' x='625' y='75054'>
                  <zone-style>
                    <format attr='border-color' value='#000000' />
                    <format attr='border-style' value='none' />
                    <format attr='border-width' value='0' />
                    <_.fcp.DashboardRoundedCorners.true...format attr='corner-radius' value='7' />
                    <format attr='margin' value='4' />
                    <format attr='padding' value='0' />
                    <format attr='background-color' value='#ffb55734' />
                  </zone-style>
                </zone>
              </zone>
              <zone-style>
                <format attr='border-color' value='#000000' />
                <format attr='border-style' value='none' />
                <format attr='border-width' value='0' />
                <format attr='margin' value='8' />
              </zone-style>
            </zone>
          </zones>
        </devicelayout>
      </devicelayouts>
      <simple-id uuid='{315D177F-7430-41C7-8199-57E8622CBE61}' />
    </dashboard>
  </dashboards>
  <windows pres-mode='true' source-height='30'>
    <window class='worksheet' name='Demografi 1'>
      <cards>
        <edge name='left'>
          <strip size='160'>
            <card type='pages' />
            <card type='filters' />
            <card type='marks' />
          </strip>
        </edge>
        <edge name='top'>
          <strip size='2147483647'>
            <card type='columns' />
          </strip>
          <strip size='2147483647'>
            <card type='rows' />
          </strip>
          <strip size='31'>
            <card type='title' />
          </strip>
        </edge>
        <edge name='right'>
          <strip size='160'>
            <card pane-specification-id='0' param='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Jenis Kelamin:nk]' type='color' />
          </strip>
        </edge>
      </cards>
      <viewpoint>
        <highlight>
          <color-one-way>
            <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Jenis Kelamin:nk]</field>
          </color-one-way>
        </highlight>
      </viewpoint>
      <simple-id uuid='{36840065-AFC1-40EE-B791-FF7B1BA684CC}' />
    </window>
    <window class='worksheet' name='jam belajar perhari'>
      <cards>
        <edge name='left'>
          <strip size='160'>
            <card type='pages' />
            <card type='filters' />
            <card type='marks' />
          </strip>
        </edge>
        <edge name='top'>
          <strip size='2147483647'>
            <card type='columns' />
          </strip>
          <strip size='2147483647'>
            <card type='rows' />
          </strip>
          <strip size='31'>
            <card type='title' />
          </strip>
        </edge>
        <edge name='right'>
          <strip size='160'>
            <card pane-specification-id='0' param='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Jam Belajar per Hari:nk]' type='color' />
          </strip>
        </edge>
      </cards>
      <viewpoint>
        <highlight>
          <color-one-way>
            <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[:Measure Names]</field>
            <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Frekuensi Belajar:nk]</field>
            <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Metode: AI Tools:qk]</field>
          </color-one-way>
        </highlight>
      </viewpoint>
      <simple-id uuid='{4AF7A3AE-88F2-4715-A2AC-1569CFCA2865}' />
    </window>
    <window class='worksheet' name='frekuensi'>
      <cards>
        <edge name='left'>
          <strip size='160'>
            <card type='pages' />
            <card type='filters' />
            <card type='marks' />
          </strip>
        </edge>
        <edge name='top'>
          <strip size='2147483647'>
            <card type='columns' />
          </strip>
          <strip size='2147483647'>
            <card type='rows' />
          </strip>
          <strip size='31'>
            <card type='title' />
          </strip>
        </edge>
        <edge name='right'>
          <strip size='160'>
            <card pane-specification-id='0' param='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:Frekuensi Belajar:qk]' type='size' />
            <card pane-specification-id='0' param='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Frekuensi Belajar:nk]' type='color' />
          </strip>
        </edge>
      </cards>
      <viewpoint>
        <highlight>
          <color-one-way>
            <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:Frekuensi Belajar:qk]</field>
            <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Frekuensi Belajar:nk]</field>
          </color-one-way>
        </highlight>
      </viewpoint>
      <simple-id uuid='{192FEDB6-2D7A-4D3A-85B8-B0C0B73541A7}' />
    </window>
    <window class='worksheet' name='IPK Distribution'>
      <cards>
        <edge name='left'>
          <strip size='160'>
            <card type='pages' />
            <card type='filters' />
            <card type='marks' />
          </strip>
        </edge>
        <edge name='top'>
          <strip size='2147483647'>
            <card type='columns' />
          </strip>
          <strip size='2147483647'>
            <card type='rows' />
          </strip>
          <strip size='31'>
            <card type='title' />
          </strip>
        </edge>
        <edge name='right'>
          <strip size='160'>
            <card pane-specification-id='0' param='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Rentang IPK:nk]' type='color' />
          </strip>
        </edge>
      </cards>
      <viewpoint>
        <selection-collection>
          <tuple-selection>
            <tuple-reference>
              <tuple-descriptor>
                <pane-descriptor>
                  <x-fields>
                    <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]</field>
                  </x-fields>
                  <y-fields>
                    <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Rentang IPK:nk]</field>
                  </y-fields>
                </pane-descriptor>
                <columns>
                  <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[cnt:No:qk]</field>
                  <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Rentang IPK:nk]</field>
                </columns>
              </tuple-descriptor>
              <tuple>
                <value>3</value>
                <value>&quot;3.50-4.00&quot;</value>
              </tuple>
            </tuple-reference>
          </tuple-selection>
        </selection-collection>
        <highlight>
          <color-one-way>
            <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Frekuensi Belajar:nk]</field>
            <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Rentang IPK:nk]</field>
          </color-one-way>
        </highlight>
      </viewpoint>
      <simple-id uuid='{251CA683-8BAA-4D2A-99DB-550CB81349D4}' />
    </window>
    <window class='worksheet' name='Waktu Belajar Favorit'>
      <cards>
        <edge name='left'>
          <strip size='160'>
            <card type='pages' />
            <card type='filters' />
            <card type='marks' />
          </strip>
        </edge>
        <edge name='top'>
          <strip size='2147483647'>
            <card type='columns' />
          </strip>
          <strip size='2147483647'>
            <card type='rows' />
          </strip>
          <strip size='31'>
            <card type='title' />
          </strip>
        </edge>
        <edge name='right'>
          <strip size='160'>
            <card pane-specification-id='0' param='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Tempat Belajar:nk]' type='color' />
          </strip>
        </edge>
      </cards>
      <viewpoint>
        <highlight>
          <color-one-way>
            <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Tempat Belajar:nk]</field>
          </color-one-way>
        </highlight>
      </viewpoint>
      <simple-id uuid='{45228115-0A11-4732-B074-87D4812440DA}' />
    </window>
    <window class='worksheet' name='Tempat Belajar'>
      <cards>
        <edge name='left'>
          <strip size='160'>
            <card type='pages' />
            <card type='filters' />
            <card type='marks' />
          </strip>
        </edge>
        <edge name='top'>
          <strip size='2147483647'>
            <card type='columns' />
          </strip>
          <strip size='2147483647'>
            <card type='rows' />
          </strip>
          <strip size='31'>
            <card type='title' />
          </strip>
        </edge>
        <edge name='right'>
          <strip size='160'>
            <card pane-specification-id='0' param='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Tempat Belajar:nk]' type='color' />
          </strip>
        </edge>
      </cards>
      <viewpoint>
        <highlight>
          <color-one-way>
            <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Tempat Belajar:nk]</field>
          </color-one-way>
        </highlight>
      </viewpoint>
      <simple-id uuid='{6ADD48BC-4CA6-48B2-BE5A-06A1BB65E82F}' />
    </window>
    <window class='worksheet' name='Metode Belajar'>
      <cards>
        <edge name='left'>
          <strip size='160'>
            <card type='pages' />
            <card type='filters' />
            <card type='marks' />
            <card type='measures' />
          </strip>
        </edge>
        <edge name='top'>
          <strip size='2147483647'>
            <card type='columns' />
          </strip>
          <strip size='2147483647'>
            <card type='rows' />
          </strip>
          <strip size='31'>
            <card type='title' />
          </strip>
        </edge>
        <edge name='right'>
          <strip size='160'>
            <card pane-specification-id='0' param='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[Multiple Values]' type='color' />
          </strip>
        </edge>
      </cards>
      <viewpoint>
        <highlight>
          <color-one-way>
            <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[:Measure Names]</field>
            <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Metode: Video:qk]</field>
          </color-one-way>
        </highlight>
      </viewpoint>
      <simple-id uuid='{1EA5A05B-5806-4597-BE67-B2B41314DB54}' />
    </window>
    <window class='worksheet' name='Korelasi Tingkat Distraksi vs Skor Kepuasan'>
      <cards>
        <edge name='left'>
          <strip size='160'>
            <card type='pages' />
            <card type='filters' />
            <card type='marks' />
          </strip>
        </edge>
        <edge name='top'>
          <strip size='2147483647'>
            <card type='columns' />
          </strip>
          <strip size='2147483647'>
            <card type='rows' />
          </strip>
          <strip size='31'>
            <card type='title' />
          </strip>
        </edge>
        <edge name='right'>
          <strip size='160'>
            <card pane-specification-id='0' param='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Tingkat Distraksi:qk]' type='color' />
          </strip>
        </edge>
      </cards>
      <viewpoint>
        <highlight>
          <color-one-way>
            <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Jam Belajar per Hari:nk]</field>
            <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Rentang IPK:nk]</field>
            <field>[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[sum:Tingkat Distraksi:qk]</field>
          </color-one-way>
        </highlight>
      </viewpoint>
      <simple-id uuid='{794C0EC8-53CE-4001-B5C9-E3AA07D0CE66}' />
    </window>
    <window class='worksheet' name='KPI Cards'>
      <cards>
        <edge name='left'>
          <strip size='160'>
            <card type='pages' />
            <card type='filters' />
            <card type='marks' />
          </strip>
        </edge>
        <edge name='top'>
          <strip size='2147483647'>
            <card type='columns' />
          </strip>
          <strip size='2147483647'>
            <card type='rows' />
          </strip>
          <strip size='31'>
            <card type='title' />
          </strip>
        </edge>
      </cards>
      <simple-id uuid='{2AD33176-BBCB-4110-A932-B1E9414DE1E2}' />
    </window>
    <window class='dashboard' maximized='true' name='Main Dashboard'>
      <viewpoints>
        <viewpoint name='Demografi 1'>
          <highlight field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Jenis Kelamin:nk]'>
            <bucket-selection />
          </highlight>
        </viewpoint>
        <viewpoint name='IPK Distribution'>
          <highlight field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Rentang IPK:nk]'>
            <bucket-selection />
          </highlight>
        </viewpoint>
        <viewpoint name='KPI Cards' />
        <viewpoint name='Korelasi Tingkat Distraksi vs Skor Kepuasan'>
          <zoom type='entire-view' />
        </viewpoint>
        <viewpoint name='Metode Belajar'>
          <zoom type='entire-view' />
        </viewpoint>
        <viewpoint name='Tempat Belajar'>
          <zoom type='entire-view' />
          <highlight field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Tempat Belajar:nk]'>
            <bucket-selection />
          </highlight>
        </viewpoint>
        <viewpoint name='Waktu Belajar Favorit'>
          <highlight field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Tempat Belajar:nk]'>
            <bucket-selection />
          </highlight>
        </viewpoint>
        <viewpoint name='frekuensi'>
          <zoom type='entire-view' />
        </viewpoint>
        <viewpoint name='jam belajar perhari'>
          <zoom type='entire-view' />
          <highlight field='[federated.0p3rgfq0q1b9nf14v4qvk0ng0lvm].[none:Jam Belajar per Hari:nk]'>
            <bucket-selection />
          </highlight>
        </viewpoint>
      </viewpoints>
      <active id='2' />
      <simple-id uuid='{B6E66F1B-0EA0-4120-B589-1C504F9AB026}' />
    </window>
  </windows>
  <thumbnails>
    <thumbnail height='128' name='Demografi 1' width='288'>
      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
      AABJRU5ErkJggg==
    </thumbnail>
    <thumbnail height='198' name='IPK Distribution' width='384'>
      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
      s2appaVFFy5c6HHc5/OpsLBQQUFBmjlz5kOeHTC6EACMKZmZmZKkU6dO9TheUlKi+vp6PfbY
      Y133DACrCADGlJSUFMXExKioqEgnTpwIGKurq9PevXslScuXL3/4kwNGGZ4GijGntLRUO3fu
      1J07d/TEE08oMTFRbrdb+fn5qq+vV0ZGhl5//XU5HI6RniowoggAxqRLly5p165dAd8ICgoK
      0sqVK7Vu3Tpe/AERAIxhPp9PVVVVunr1qqKiopSQkNDvj8QASwgAABjFTWAAMIoAAIBRBAAA
      jCIAAGAUAQAAowgAABhFAADAKAIAAEYRAAAwigAAgFEEAACMIgAAYBQBAACjCAAAGEUAAMAo
      AgAARhEAADCKAACAUQQAAIwiAABgFAEAAKMIAAAYRQAAwCgCAABGEQAAMIoAAIBRBAAAjCIA
      AGAUAQAAowgAABhFAADAKAIAAEYRAAAwigAAgFEEAACMIgAAYBQBAACjCAAAGEUAAMAoAgAA
      RhEAADCKAACAUQQAAIwiAABgFAEAAKMIAAAYRQAAwCgCAABGEQAAMIoAAIBRBAAAjCIAAGAU
      AQAAowgAABhFAADAKAIAAEYRAAAwigAAgFEEAACMIgAAYNT/AREdSzn/nBHoAAAAAElFTkSu
      QmCC
    </thumbnail>
    <thumbnail height='94' name='KPI Cards' width='208'>
      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
      RK5CYII=
    </thumbnail>
    <thumbnail height='384' name='Korelasi Tingkat Distraksi vs Skor Kepuasan' width='384'>
      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
      AACGIgAAwFAEAAAYigAAAEMRAABgKAIAAAxFAACAoQgAADAUAQAAhiIAAMBQBAAAGIoAAABD
      EQAAYCgCAAAMRQAAgKEIAAAwFAEAAIYiAADAUAQAABiKAAAAQxEAAGAoAgAADEUAAIChCAAA
      MBQBAACGIgAAwFAEAAAYigAAAEMRAABgKAIAAAxFAACAoQgAADAUAQAAhiIAAMBQBAAAGIoA
      AABDEQAAYCgCAAAMRQAAgKEIAAAwFAEAAIYiAADAUAQAABiKAAAAQxEAAGAoAgAADEUAAICh
      CAAAMBQBAACGIgAAwFAEAAAYigAAAEMRAABgKAIAAAxFAACAoQgAADAUAQAAhiIAAMBQBAAA
      GMqzAIjFYkokEl7tHgCMl/UAcBxH69at0+9//3vt27cv27sHAHwu6wEQj8dlWZbmzJmjZDKZ
      7d0DAD5nua7rerHj9evXq7i4WBMnTpQkua4rx3G6t9u2TUCcIJlMyrIsWZbldSk5o+vjS5v0
      5DiO/H6/12XklGQyKZ+Pac8u/fr1swJeF3Eyfr9feXl5XpeRU+LxuPx+P1/s49i2LUkKBHL2
      o+yJzs5OhcNhr8vIKbRJqpz51liW1eNLbNs2Z3UnQbukok1S0Sbp0S5fyHoAtLS0qLq6Wp9+
      +qkaGxtl27amTp2a7TIAwHhZDwCfz6f8/HxNnz79WAF03QHAE1k/+g4YMECTJk3K9m4BACdg
      ShwADEUAAIChCAAAMBQBAACGIgAAwFAEAAAYigAAAEMRAABgKAIAAAxFAACAoQgAADAUAQAA
      hiIAAMBQBAAAGIoAAABDEQAAYCgCAAAMRQAAgKEIAAAwFAEAAIYiAADAUAQAABiKAAAAQxEA
      AGAoAgAADEUAAIChCAAAMBQBAACGIgAAwFAEAAAYigAAAEMRAABgKAIAAAxFAACAoQgAADAU
      AQAAhiIAAMBQBAAAGIoAAABDEQAAYCgCAAAMRQAAgKEIAAAwFAEAAIYiAADAUAQAABiKAAAA
      QxEAAGAoAgAADEUAAIChCAAAMBQBAACGIgAAwFAEAAAYypMASCaTam1tVTwe92L3AABJgWzv
      MJlMaunSpbJtWx0dHVq8eLGKi4uzXQYAGC/rPYADBw7I5/Ppe9/7nubNm6c1a9ZkuwQAgDwI
      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
    </thumbnail>
    <thumbnail height='384' name='Main Dashboard' width='384'>
      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
    </thumbnail>
    <thumbnail height='384' name='Metode Belajar' width='384'>
      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
      RU5ErkJggg==
    </thumbnail>
    <thumbnail height='128' name='Tempat Belajar' width='288'>
      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
    </thumbnail>
    <thumbnail height='242' name='Waktu Belajar Favorit' width='384'>
      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
      tqmpSX6/X5mZmf1+ti4N/eOa8+fPS5KmT58+pO0AjD0EYBQoLCyU3+/X1q1bFQgEBv3kr9Pp
      lM1m04kTJ9TR0RGxLBAI6IcfftCPP/44pFl67/zp7yllj8ejd999V8FgcEj7BDA6cQ1gFJg/
      f762b9+u8vJyJScna/bs2YPaLi4uTrfffruOHj2qTZs2qaCgQOnp6aqpqQk/xTt+/PghzTJv
      3jwVFxdr9+7d8vl8mjt3rlpaWlRdXa2qqiolJ/ML94BYQQBGiM1mk2VZEffq90pOTtZtt92m
      qqoquVwu2Wx9T8z6206S1q1bp46ODp06dSp8sdeyLE2fPl3r16/XuXPn9M033wy4v3/uNzs7
      W+vXr9f27dtVUlKikpISSVe+inrJkiVatWqVXn755QF/zoHmtNlsAy6z2+2yLGvAfQK4MawQ
      9/TFBI/Ho8bGRiUmJionJ0eJiYnXtT+/36+6ujq1trYqOztbGRkZo/Ig7ff75Ti8J9pjAGMS
      AcCYRgCAf4+LwABgKAIAAIYiAABgKAIAAIbiIjDGNL/fL4fDEe0xMIq0tbVJEs+sDAJnAABg
      KAIAAIYiAABgKAIAAIYiAABgKAIAAIYiAABgKAIAAIYiAABgKH4hDMa+/+6M9gQYRZIltbmW
      RHuMMYEzAAAwFAEAAEMRAAAwFNcAYlR9fb0uXLjQ5/UJEyYoIyNDKSkpUZiqr1AopP3796un
      p0dFRUWKj4+P9kiAMQhAjDp48KB++umnAZdPnDhRK1asUFFRkWy26J0IBoNBbd26VZLkcrkI
      ADCCCECMe/DBB5WVlSXpysG2ublZHo9HZWVl2rp1q2pra/XEE09EbT7LsjRnzhzZ7XYlJCRE
      bQ7ARAQgxs2ZM0ezZs3q8/qFCxf0zjvvaN++fbrjjjuUl5cXhekkm82m559/Pip/N2A6LgIb
      asqUKXr88cclSZWVlVGeBkA0cAZgsNzcXElXLhj/XSAQUGVlpSoqKuTz+XTx4kXZ7XZlZGRo
      /vz5crlcA+4zGAxq3759OnPmjOrr6xUMBpWamqrc3FylpKSou7tbixcvjtjmu+++U3d3tx55
      5JHh/yEBDIgAGCwu7sp//p6enojXP/jgA506dUqSlJSUpPT0dPn9fh07dkxlZWU6evSoNm7c
      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
      NenQoUNqbm7WPffcoyeeeIIvC4sBu3fvVmNjY8RrjY2NOnPmjHJycpSVlRV+PTExUY8++uhI
      jziqEQDEpJqaGm3ZsiXijiCbzaalS5dq9erVHPxjxPvvv6+TJ08Oat2JEyfq7bffvsETjS0E
      ADErFAqpoaFBtbW1mjhxonJycq75kBhgEgIAAIbiIjAAGIoAAIChCAAAGIoAAIChCAAAGIoA
      AIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoA
      AIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoA
      AIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoA
      AIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoA
      AIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoAAIChCAAAGIoA
      AIChCAAAGIoAAICh/gcW3kG5q9WijgAAAABJRU5ErkJggg==
    </thumbnail>
    <thumbnail height='248' name='frekuensi' width='248'>
      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
      RK5CYII=
    </thumbnail>
    <thumbnail height='384' name='jam belajar perhari' width='384'>
      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
    </thumbnail>
  </thumbnails>
</workbook>
