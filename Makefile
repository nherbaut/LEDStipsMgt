build:
	docker buildx build --platform linux/amd64,linux/arm64 -t nherbaut/led_stip_mgt:latest  .
push:
	docker buildx build --platform linux/amd64,linux/arm64 -t nherbaut/led_stip_mgt:latest --push .
run:
	docker pull nherbaut/led_stip_mgt:latest && docker run --rm --name led -v ./profiles:/code/profiles -v ./presets:/code/presets -p 8080:80 nherbaut/led_stip_mgt:latest
