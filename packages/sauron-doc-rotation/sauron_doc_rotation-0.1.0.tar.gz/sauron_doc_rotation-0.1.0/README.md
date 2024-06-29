## Sauron-doc-rotation

The Sauron DOC rotation is a simple project that aims to rotate a base64 image to keep it in the correct direction.

### How to use?

You can use the **rotate_image_base64** method in **sauron_rotate** to rotate your base64 image.

The following code shows how you can use this method.

```python
from sauron_doc_rotate.sauron_rotate import SauronRotate

sr = SauronRotate(enable_logging=False)

sr.rotate_image_base64(img_base64)
```

* Method / Class parameters
  * `enable_logging` - whether or not to show logs during code execution 

* Method returns
  * A dict with two values:
    * `angles_for_rotation` - the angles tuple used to rotate the imagem  
    * `rotated_img_base64` - the base64 image in the correct direction