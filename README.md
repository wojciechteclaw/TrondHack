# S.A.M.B.A. - Speckle as Material Bank App

This is the result of a 3-days work on the Speckle hackathon "Into the Speckleverse" https://hack.speckle.dev/, where we* protoyped the solution called SAMBA.

We* are engineers and architects who on daily basis research how to make buildings more sustainable. One way to do that is by applying circular practices, in particular - the reuse of building components. But this is not that easy. First you need to know what elements are available. Then there is a challange of mapping those to your new design. 

Our proposed workflow is based on Speckle app that allows for convinient data exchange between AEC software. 
### Adding elements to SAMBA:
1. First, we send out BIM models as they are from software such as Revit or Archicad, to the Speckle branch: 'RAW_MODELS' https://speckle.xyz/streams/4ddb373003/branches/main.
2. Then, the Grasshopper script is receiving data automatically and preprocess it by extracting reusable elements and arranging them in desired form. Such aggregation is then sent to 'PREPROCESSED' branch: https://speckle.xyz/streams/adda68dad6
3. Next step is our Python service that is triggered by Speckle webhooks when a new model arrives. It reads the content and appends data such as Life Cycle Assesment (LCA) calculations. 
4. After that, the same Python service appends those elements to the Material Bank branch: https://speckle.xyz/streams/8e9249d66e

### Using elements from SAMBA:
1. Designer who wants to use components from the Material Bank can receive the elements using Speckle.
2. Then we have preparrred a mapping script that tries to fit 'used' elements to 'new' design by genetic algorithm in Galapagos plugin.
3. After succesfull selection of elements, the designer notifies the bank that he wants to take some elements by updating the bank.

### \* The TrondHack team:
* Weronika Budnik, https://github.com/boniqa
* Marcin Łuczkowski, https://github.com/marcinluczkowski
* Wojciech Tecław, https://github.com/wojciechteclaw
* Artur Tomczak, https://github.com/atomczak

![TrondHack.jpg](/media/TrondHack.jpg)
