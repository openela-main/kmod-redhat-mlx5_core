%define kmod_name		mlx5_core
%define kmod_vendor		redhat
%define kmod_rpm_name		kmod-redhat-mlx5_core
%define kmod_driver_version	5.0_0_dup8.2
%define kmod_driver_epoch	%{nil}
%define kmod_rpm_release	2
%define kmod_kernel_version	4.18.0-193.el8
%define kmod_kernel_version_min	%{nil}
%define kmod_kernel_version_dep	%{nil}
%define kmod_kbuild_dir		drivers/net/ethernet/mellanox/mlx5/core
%define kmod_dependencies       %{nil}
%define kmod_dist_build_deps	%{nil}
%define kmod_build_dependencies	%{nil}
%define kmod_devel_package	1
%define kmod_devel_src_paths	include
%define kmod_install_path	extra/kmod-redhat-mlx5_core
%define kernel_pkg		kernel
%define kernel_devel_pkg	kernel-devel
%define kernel_modules_pkg	kernel-modules

%{!?dist: %define dist .el8_2}
%{!?make_build: %define make_build make}

%if "%{kmod_kernel_version_dep}" == ""
%define kmod_kernel_version_dep %{kmod_kernel_version}
%endif

%if "%{kmod_dist_build_deps}" == ""
%if (0%{?rhel} > 7) || (0%{?centos} > 7)
%define kmod_dist_build_deps redhat-rpm-config kernel-abi-whitelists elfutils-libelf-devel kernel-rpm-macros kmod
%else
%define kmod_dist_build_deps redhat-rpm-config kernel-abi-whitelists
%endif
%endif

Source0:	%{kmod_name}-%{kmod_vendor}-%{kmod_driver_version}.tar.bz2
# Source code patches
Patch0:	0001-netdrv-mlx5e-allow-TSO-on-VXLAN-over-VLAN-topologies.patch
Patch1:	0002-netdrv-net-reject-PTP-periodic-output-requests-with-.patch
Patch2:	0003-netdrv-mlx5-reject-unsupported-external-timestamp-fl.patch
Patch3:	0004-netdrv-mlx5e-Reorder-mirrer-action-parsing-to-check-.patch
Patch4:	0005-netdrv-net-mlx5e-Move-the-SW-XSK-code-from-NAPI-poll.patch
Patch5:	0006-netdrv-mlx5e-Allow-XSK-frames-smaller-than-a-page.patch
Patch6:	0007-netdrv-net-Use-skb-accessors-in-network-drivers.patch
Patch7:	0008-netdrv-net-mlx5e-xsk-dynamically-allocate-mlx5e_chan.patch
Patch8:	0009-netdrv-net-mlx5-E-Switch-add-ingress-rate-support.patch
Patch9:	0010-netdrv-net-mlx5e-Tx-Strict-the-room-needed-for-SQ-ed.patch
Patch10:	0011-netdrv-net-mlx5e-XDP-Close-TX-MPWQE-session-when-no-.patch
Patch11:	0012-netdrv-net-mlx5e-XDP-Slight-enhancement-for-WQE-fetc.patch
Patch12:	0013-netdrv-net-mlx5e-Tx-Soften-inline-mode-VLAN-dependen.patch
Patch13:	0014-netdrv-net-mlx5e-Rx-checksum-handling-refactoring.patch
Patch14:	0015-netdrv-net-mlx5e-Set-tx-reporter-only-on-successful-.patch
Patch15:	0016-netdrv-net-mlx5e-TX-reporter-cleanup.patch
Patch16:	0017-netdrv-net-mlx5e-Allow-dropping-specific-tunnel-pack.patch
Patch17:	0018-netdrv-mlx5-no-need-to-check-return-value-of-debugfs.patch
Patch18:	0019-netdrv-net-mlx5-Use-debug-message-instead-of-warn.patch
Patch19:	0020-netdrv-net-mlx5-Add-XRQ-legacy-commands-opcodes.patch
Patch20:	0021-netdrv-net-mlx5e-Rename-reporter-header-file.patch
Patch21:	0022-netdrv-net-mlx5e-Change-naming-convention-for-report.patch
Patch22:	0023-netdrv-net-mlx5e-Generalize-tx-reporter-s-functional.patch
Patch23:	0024-netdrv-net-mlx5e-Extend-tx-diagnose-function.patch
Patch24:	0025-netdrv-net-mlx5e-Extend-tx-reporter-diagnostics-outp.patch
Patch25:	0026-netdrv-net-mlx5e-Add-cq-info-to-tx-reporter-diagnose.patch
Patch26:	0027-netdrv-net-mlx5e-Add-helper-functions-for-reporter-s.patch
Patch27:	0028-netdrv-net-mlx5e-Add-support-to-rx-reporter-diagnose.patch
Patch28:	0029-netdrv-net-mlx5e-Split-open-close-ICOSQ-into-stages.patch
Patch29:	0030-netdrv-net-mlx5e-Report-and-recover-from-CQE-error-o.patch
Patch30:	0031-netdrv-net-mlx5e-Report-and-recover-from-rx-timeout.patch
Patch31:	0032-netdrv-net-mlx5e-RX-Handle-CQE-with-error-at-the-ear.patch
Patch32:	0033-netdrv-net-mlx5e-Report-and-recover-from-CQE-with-er.patch
Patch33:	0034-netdrv-net-mlx5-Improve-functions-documentation.patch
Patch34:	0035-include-net-mlx5-Expose-IP-in-IP-capability-bit.patch
Patch35:	0036-netdrv-net-mlx5-Add-per-namespace-flow-table-default.patch
Patch36:	0037-netdrv-net-mlx5-Create-bypass-and-loopback-flow-stee.patch
Patch37:	0038-netdrv-net-mlx5e-Add-tc-flower-tracepoints.patch
Patch38:	0039-netdrv-net-mlx5e-Add-trace-point-for-neigh-used-valu.patch
Patch39:	0040-netdrv-net-mlx5e-Add-trace-point-for-neigh-update.patch
Patch40:	0041-netdrv-net-mlx5-Add-wrappers-for-HyperV-PCIe-operati.patch
Patch41:	0042-netdrv-net-mlx5-Fix-return-code-in-case-of-hyperv-wr.patch
Patch42:	0043-netdrv-net-mlx5-Set-ODP-capabilities-for-DC-transpor.patch
Patch43:	0044-netdrv-net-mlx5e-Change-function-s-position-to-a-mor.patch
Patch44:	0045-netdrv-net-mlx5e-Support-RSS-for-IP-in-IP-and-IPv6-t.patch
Patch45:	0046-netdrv-net-mlx5e-Improve-stateless-offload-capabilit.patch
Patch46:	0047-netdrv-net-mlx5e-Support-TSO-and-TX-checksum-offload.patch
Patch47:	0048-netdrv-net-mlx5e-Remove-unlikely-from-WARN-condition.patch
Patch48:	0049-netdrv-net-mlx5-Kconfig-Fix-MLX5_CORE-dependency-wit.patch
Patch49:	0050-netdrv-net-mlx5e-Use-ipv6_stub-to-avoid-dependency-w.patch
Patch50:	0051-netdrv-net-mlx5-Use-PTR_ERR_OR_ZERO-rather-than-its-.patch
Patch51:	0052-netdrv-net-mlx5e-kTLS-Remove-unused-function-paramet.patch
Patch52:	0053-netdrv-net-mlx5-DR-Remove-useless-set-memory-to-zero.patch
Patch53:	0054-netdrv-net-mlx5-DR-Remove-redundant-dev_name-print-f.patch
Patch54:	0055-netdrv-drivers-net-Fix-Kconfig-indentation.patch
Patch55:	0056-netdrv-net-mlx5e-kTLS-Release-reference-on-DUMPed-fr.patch
Patch56:	0057-netdrv-net-mlx5e-kTLS-Size-of-a-Dump-WQE-is-fixed.patch
Patch57:	0058-netdrv-net-mlx5e-kTLS-Save-only-the-frag-page-to-rel.patch
Patch58:	0059-netdrv-net-mlx5e-kTLS-Save-by-value-copy-of-the-reco.patch
Patch59:	0060-netdrv-net-mlx5e-kTLS-Fix-page-refcnt-leak-in-TX-res.patch
Patch60:	0061-netdrv-net-mlx5e-kTLS-Fix-missing-SQ-edge-fill.patch
Patch61:	0062-netdrv-net-mlx5e-kTLS-Limit-DUMP-wqe-size.patch
Patch62:	0063-netdrv-net-mlx5e-kTLS-Remove-unneeded-cipher-type-ch.patch
Patch63:	0064-netdrv-net-mlx5e-kTLS-Save-a-copy-of-the-crypto-info.patch
Patch64:	0065-netdrv-net-mlx5e-kTLS-Enhance-TX-resync-flow.patch
Patch65:	0066-netdrv-net-mlx5e-Remove-incorrect-match-criteria-ass.patch
Patch66:	0067-netdrv-mlx5-reject-unsupported-external-timestamp-fl.patch
Patch67:	0068-netdrv-net-mlx5e-Fix-ingress-rate-configuration-for-.patch
Patch68:	0069-netdrv-net-mlx5e-Add-missing-capability-bit-check-fo.patch
Patch69:	0070-include-net-mlx5-Expose-optimal-performance-scatter-.patch
Patch70:	0071-netdrv-net-Fix-misspellings-of-configure-and-configu.patch
Patch71:	0072-netdrv-net-mlx5-E-Switch-Rename-egress-config-to-gen.patch
Patch72:	0073-netdrv-net-mlx5-E-Switch-Rename-ingress-acl-config-i.patch
Patch73:	0074-netdrv-net-mlx5-E-switch-Introduce-and-use-vlan-rule.patch
Patch74:	0075-netdrv-net-mlx5-Introduce-and-use-mlx5_esw_is_manage.patch
Patch75:	0076-netdrv-net-mlx5-Move-metdata-fields-under-offloads-s.patch
Patch76:	0077-netdrv-net-mlx5-Move-legacy-drop-counter-and-rule-un.patch
Patch77:	0078-netdrv-net-mlx5-Tide-up-state_lock-and-vport-enabled.patch
Patch78:	0079-netdrv-net-mlx5-E-switch-Prepare-code-to-handle-vpor.patch
Patch79:	0080-netdrv-net-mlx5-E-switch-Legacy-introduce-and-use-pe.patch
Patch80:	0081-netdrv-net-mlx5-Move-ACL-drop-counters-life-cycle-cl.patch
Patch81:	0082-netdrv-net-mlx5-E-switch-Offloads-introduce-and-use-.patch
Patch82:	0083-netdrv-net-mlx5-E-switch-Offloads-shift-ACL-programm.patch
Patch83:	0084-netdrv-net-mlx5-Restrict-metadata-disablement-to-off.patch
Patch84:	0085-netdrv-net-mlx5-Refactor-ingress-acl-configuration.patch
Patch85:	0086-netdrv-net-mlx5-FPGA-support-network-cards-with-stan.patch
Patch86:	0087-netdrv-net-mlx5-Remove-unneeded-variable-in-mlx5_unl.patch
Patch87:	0088-netdrv-net-mlx5e-Verify-that-rule-has-at-least-one-f.patch
Patch88:	0089-netdrv-net-mlx5-Do-not-hold-group-lock-while-allocat.patch
Patch89:	0090-netdrv-net-mlx5-Support-lockless-FTE-read-lookups.patch
Patch90:	0091-netdrv-net-mlx5e-TX-Dump-WQs-wqe-descriptors-on-CQE-.patch
Patch91:	0092-netdrv-net-mlx5-WQ-Move-short-getters-into-header-fi.patch
Patch92:	0093-netdrv-net-mlx5e-Bit-sized-fields-rewrite-support.patch
Patch93:	0094-netdrv-net-mlx5e-Add-ToS-DSCP-header-rewrite-support.patch
Patch94:	0095-netdrv-net-mlx5-rate-limit-alloc_ent-error-messages.patch
Patch95:	0096-netdrv-net-mlx5-LAG-Use-port-enumerators.patch
Patch96:	0097-netdrv-net-mlx5-fix-kvfree-of-uninitialized-pointer-.patch
Patch97:	0098-netdrv-net-mlx5-fix-spelling-mistake-metdata-metadat.patch
Patch98:	0099-netdrv-net-mlx5-Dump-of-fw_fatal-use-updated-devlink.patch
Patch99:	0100-netdrv-net-mlx5-Simplify-fdb-chain-and-prio-eswitch-.patch
Patch100:	0101-netdrv-net-mlx5-Rename-FDB_-tc-related-defines-to-FD.patch
Patch101:	0102-netdrv-net-mlx5-Define-fdb-tc-levels-per-prio.patch
Patch102:	0103-netdrv-net-mlx5-Accumulate-levels-for-chains-prio-na.patch
Patch103:	0104-netdrv-net-mlx5-Refactor-creating-fast-path-prio-cha.patch
Patch104:	0105-netdrv-net-mlx5-Add-new-chain-for-netfilter-flow-tab.patch
Patch105:	0106-netdrv-net-mlx5-Remove-redundant-NULL-initialization.patch
Patch106:	0107-netdrv-net-mlx5-Don-t-write-read-only-fields-in-MODI.patch
Patch107:	0108-netdrv-net-mlx5-DR-Refactor-VXLAN-GPE-flex-parser-tu.patch
Patch108:	0109-netdrv-net-mlx5-DR-Add-HW-bits-and-definitions-for-G.patch
Patch109:	0110-netdrv-net-mlx5-DR-Add-support-for-Geneve-packets-SW.patch
Patch110:	0111-netdrv-net-mlx5e-TC-Stub-out-ipv6-tun-create-header-.patch
Patch111:	0112-netdrv-net-mlx5e-Remove-redundant-pointer-check.patch
Patch112:	0113-netdrv-net-use-rhashtable_lookup-instead-of-rhashtab.patch
Patch113:	0114-netdrv-net-mlx5e-Fix-build-error-without-IPV6.patch
Patch114:	0115-netdrv-net-mlx5e-E-switch-Fix-Ingress-ACL-groups-in-.patch
Patch115:	0116-netdrv-treewide-Use-sizeof_field-macro.patch
Patch116:	0117-netdrv-net-mlx5e-Avoid-duplicating-rule-destinations.patch
Patch117:	0118-netdrv-net-mlx5e-Always-print-health-reporter-messag.patch
Patch118:	0119-netdrv-net-mlx5-Move-devlink-registration-before-int.patch
Patch119:	0120-netdrv-Revert-net-mlx5-Support-lockless-FTE-read-loo.patch
Patch120:	0121-netdrv-net-mlx5e-Fix-hairpin-RSS-table-size.patch
Patch121:	0122-netdrv-net-mlx5-Fix-lowest-FDB-pool-size.patch
Patch122:	0123-netdrv-net-mlx5-Update-the-list-of-the-PCI-supported.patch
Patch123:	0124-netdrv-net-mlx5-E-Switch-Prevent-ingress-rate-config.patch
Patch124:	0125-netdrv-net-mlx5e-kTLS-Fix-corner-case-checks-in-TX-r.patch
Patch125:	0126-netdrv-net-mlx5e-kTLS-Remove-redundant-posts-in-TX-r.patch
Patch126:	0127-netdrv-net-mlx5e-kTLS-Do-not-send-decrypted-marked-S.patch
Patch127:	0128-netdrv-net-mlx5-limit-the-function-in-local-scope.patch
Patch128:	0129-netdrv-mlx5-work-around-high-stack-usage-with-gcc.patch
Patch129:	0130-netdrv-net-mlx5e-Support-accept-action-on-nic-table.patch
Patch130:	0131-netdrv-net-mlx5-Increase-the-max-number-of-channels-.patch
Patch131:	0132-netdrv-net-mlx5-Reduce-No-CQ-found-log-level-from-wa.patch
Patch132:	0133-netdrv-net-mlx5-Use-async-EQ-setup-cleanup-helpers-f.patch
Patch133:	0134-include-net-mlx5-Add-Virtio-Emulation-related-device.patch
Patch134:	0135-netdrv-net-mlx5-Expose-vDPA-emulation-device-capabil.patch
Patch135:	0136-include-net-mlx5-Add-RoCE-accelerator-counters.patch
Patch136:	0137-include-net-mlx5-Expose-relaxed-ordering-bits.patch
Patch137:	0138-include-net-mlx5-Add-copy-header-action-struct-layou.patch
Patch138:	0139-include-net-mlx5-Add-mlx5_ifc-definitions-for-connec.patch
Patch139:	0140-include-net-mlx5e-Expose-FEC-feilds-and-related-capa.patch
Patch140:	0141-netdrv-net-mlx5-Refactor-mlx5_create_auto_grouped_fl.patch
Patch141:	0142-netdrv-net-mlx5-fs_core-Introduce-unmanaged-flow-tab.patch
Patch142:	0143-netdrv-net-mlx5-Add-ignore-level-support-fwd-to-tabl.patch
Patch143:	0144-netdrv-net-mlx5-Allow-creating-autogroups-with-reser.patch
Patch144:	0145-netdrv-net-mlx5e-Fix-printk-format-warning.patch
Patch145:	0146-netdrv-net-mlx5e-Add-mlx5e_flower_parse_meta-support.patch
Patch146:	0147-netdrv-net-mlx5-DR-Modify-set-action-limitation-exte.patch
Patch147:	0148-netdrv-net-mlx5-DR-Modify-header-copy-support.patch
Patch148:	0149-netdrv-net-mlx5-DR-Allow-connecting-flow-table-to-a-.patch
Patch149:	0150-netdrv-net-mlx5-IPsec-Fix-esp-modify-function-attrib.patch
Patch150:	0151-netdrv-net-mlx5-IPsec-fix-memory-leak-at-mlx5_fpga_i.patch
Patch151:	0152-netdrv-net-mlx5e-TX-Error-completion-is-for-last-WQE.patch
Patch152:	0153-netdrv-net-mlx5-Deprecate-usage-of-generic-TLS-HW-ca.patch
Patch153:	0154-netdrv-net-mlx5-Fix-sleep-while-atomic-in-mlx5_eswit.patch
Patch154:	0155-netdrv-net-mlx5e-Reset-RQ-doorbell-counter-before-mo.patch
Patch155:	0156-netdrv-net-mlx5e-Fix-crash-in-recovery-flow-without-.patch
Patch156:	0157-netdrv-net-mlx5-DR-Fix-postsend-actions-write-length.patch
Patch157:	0158-netdrv-net-mlx5e-kTLS-Fix-TCP-seq-off-by-1-issue-in-.patch
Patch158:	0159-netdrv-net-mlx5e-kTLS-Fix-wrong-value-in-record-trac.patch
Patch159:	0160-netdrv-net-mlx5e-Fix-endianness-handling-in-pedit-ma.patch
Patch160:	0161-netdrv-net-mlx5-Clear-LAG-notifier-pointer-after-unr.patch
Patch161:	0162-netdrv-net-mlx5_core-Set-IB-capability-mask1-to-fix-.patch
Patch162:	0163-netdrv-net-mlx5e-Enhance-ICOSQ-WQE-info-fields.patch
Patch163:	0164-netdrv-net-mlx5e-Fix-missing-reset-of-SW-metadata-in.patch
Patch164:	0165-netdrv-net-mlx5e-Fix-ICOSQ-recovery-flow-with-Stridi.patch
Patch165:	0166-netdrv-net-mlx5e-Do-not-recover-from-a-non-fatal-syn.patch
Patch166:	0167-netdrv-net-mlx5e-Define-one-flow-for-TXQ-selection-w.patch
Patch167:	0168-netdrv-net-mlx5e-Add-missing-LRO-cap-check.patch
Patch168:	0169-netdrv-net-mlx5e-Encapsulate-updating-netdev-queues-.patch
Patch169:	0170-netdrv-net-mlx5e-Rename-hw_modify-to-preactivate.patch
Patch170:	0171-netdrv-net-mlx5e-Use-preactivate-hook-to-set-the-ind.patch
Patch171:	0172-netdrv-net-mlx5e-Fix-configuration-of-XPS-cpumasks-a.patch
Patch172:	0173-netdrv-net-mlx5e-Remove-unneeded-netif_set_real_num_.patch
Patch173:	0174-netdrv-net-mlx5e-Allow-mlx5e_switch_priv_channels-to.patch
Patch174:	0175-netdrv-net-mlx5e-Add-context-to-the-preactivate-hook.patch
Patch175:	0176-netdrv-net-mlx5e-Change-inline-mode-correctly-when-c.patch
Patch176:	0177-netdrv-net-mlx5e-RX-Use-indirect-calls-wrapper-for-p.patch
Patch177:	0178-netdrv-net-mlx5e-RX-Use-indirect-calls-wrapper-for-h.patch
Patch178:	0179-netdrv-net-mlx5-sparse-warning-incorrect-type-in-ass.patch
Patch179:	0180-netdrv-net-mlx5-sparse-warning-Using-plain-integer-a.patch
Patch180:	0181-include-net-mlx5-fix-spelling-mistake-reserverd-rese.patch
Patch181:	0182-netdrv-net-mlx5e-Use-netdev_warn-for-errors-for-adde.patch
Patch182:	0183-include-net-mlx5-Expose-link-speed-directly.patch
Patch183:	0184-netdrv-net-mlx5-Expose-port-speed-when-possible.patch
Patch184:	0185-netdrv-net-mlx5-Tidy-up-and-fix-reverse-christmas-or.patch
Patch185:	0186-netdrv-net-mlx5-E-Switch-Hold-mutex-when-querying-dr.patch
Patch186:	0187-netdrv-net-mlx5-Fix-group-version-management.patch
Patch187:	0188-netdrv-net-mlx5e-Don-t-allow-forwarding-between-upli.patch
Patch188:	0189-netdrv-net-mlx5-Eswitch-avoid-redundant-mask.patch
Patch189:	0190-netdrv-net-mlx5-DR-Change-matcher-priority-parameter.patch
Patch190:	0191-netdrv-net-mlx5-DR-Improve-log-messages.patch
Patch191:	0192-netdrv-net-mlx5-DR-Remove-unneeded-functions-deceler.patch
Patch192:	0193-netdrv-net-mlx5e-Use-netdev_warn-instead-of-pr_err-f.patch
Patch193:	0194-netdrv-net-mlx5e-Remove-unused-argument-from-parse_t.patch
Patch194:	0195-netdrv-flow_offload-check-for-basic-action-hw-stats-.patch
Patch195:	0196-netdrv-net-mlx5-Fix-frequent-ioread-PCI-access-durin.patch
Patch196:	0197-netdrv-net-mlx5e-Add-missing-release-firmware-call.patch
Patch197:	0198-netdrv-net-mlx5e-Fix-nest_level-for-vlan-pop-action.patch
Patch198:	0199-netdrv-net-mlx5e-Fix-pfnum-in-devlink-port-attribute.patch
Patch199:	0200-netdrv-net-mlx5-Fix-failing-fw-tracer-allocation-on-.patch
Patch200:	0201-netdrv-net-mlx5e-Don-t-trigger-IRQ-multiple-times-on.patch
Patch201:	0202-netdrv-net-mlx5e-Get-the-latest-values-from-counters.patch
Patch202:	0203-netdrv-net-mlx5-DR-On-creation-set-CQ-s-arm_db-membe.patch
Patch203:	0204-netdrv-net-mlx5-Fix-forced-completion-access-non-ini.patch
Patch204:	0205-netdrv-net-mlx5-Fix-command-entry-leak-in-Internal-E.patch
Patch205:	0206-netdrv-net-mlx5e-Fix-q-counters-on-uplink-represento.patch
Patch206:	0207-netdrv-net-mlx5e-en_accel-Add-missing-net-geneve.h-i.patch
Patch207:	0208-netdrv-net-mlx5e-Set-of-completion-request-bit-shoul.patch
Patch208:	0209-netdrv-mlx5-Update-list-of-unsupported-devices.patch
Patch209:	0210-netdrv-mlx5-Remove-the-unsupported-mark-from-Connect.patch
Patch210:	0211-netdrv-net-mlx5-TC-Offload-flow-table-rules.patch
Patch211:	0212-netdrv-net-mlx5-ft-Use-getter-function-to-get-ft-cha.patch
Patch212:	0213-netdrv-net-mlx5-ft-Check-prio-and-chain-sanity-for-f.patch
Patch213:	0214-netdrv-net-mlx5-E-Switch-Refactor-chains-and-priorit.patch
Patch214:	0215-netdrv-net-mlx5-E-Switch-Increase-number-of-chains-a.patch
Patch215:	0216-netdrv-net-mlx5-make-the-symbol-ESW_POOLS-static.patch
Patch216:	0217-netdrv-net-mlx5e-Eswitch-Use-per-vport-tables-for-mi.patch
Patch217:	0218-netdrv-net-mlx5-E-Switch-Allow-goto-earlier-chain-if.patch
Patch218:	0219-netdrv-net-mlx5e-Use-NL_SET_ERR_MSG_MOD-extack-for-e.patch
Patch219:	0220-netdrv-net-mlx5e-Reduce-number-of-arguments-in-slow-.patch
Patch220:	0221-netdrv-net-mlx5e-Remove-redundant-comment-about-goto.patch
Patch221:	0222-netdrv-net-mlx5-Verify-goto-chain-offload-support.patch
Patch222:	0223-netdrv-net-mlx5e-Fix-an-IS_ERR-vs-NULL-check.patch
Patch223:	0224-netdrv-net-mlx5-Change-the-name-of-steering-mode-par.patch
Patch224:	0225-netdrv-net-mlx5e-Add-devlink-fdb_large_groups-parame.patch
Patch225:	0226-netdrv-net-mlx5-Introduce-mapping-infra-for-mapping-.patch
Patch226:	0227-infiniband-net-mlx5-E-Switch-Move-source-port-on-reg.patch
Patch227:	0228-netdrv-net-mlx5-E-Switch-Get-reg_c0-value-on-CQE.patch
Patch228:	0229-netdrv-net-mlx5-E-Switch-Mark-miss-packets-with-new-.patch
Patch229:	0230-netdrv-net-mlx5e-Rx-Split-rep-rx-mpwqe-handler-from-.patch
Patch230:	0231-netdrv-net-mlx5-E-Switch-Restore-chain-id-on-miss.patch
Patch231:	0232-netdrv-net-mlx5e-Allow-re-allocating-mod-header-acti.patch
Patch232:	0233-netdrv-net-mlx5e-Move-tc-tunnel-parsing-logic-with-t.patch
Patch233:	0234-netdrv-net-mlx5e-Disallow-inserting-vxlan-vlan-egres.patch
Patch234:	0235-netdrv-net-mlx5e-Support-inner-header-rewrite-with-g.patch
Patch235:	0236-netdrv-net-mlx5-E-Switch-Get-reg_c1-value-on-miss.patch
Patch236:	0237-netdrv-net-mlx5e-Restore-tunnel-metadata-on-miss.patch
Patch237:	0238-netdrv-net-mlx5-E-Switch-Enable-reg-c1-loopback-when.patch
Patch238:	0239-netdrv-net-mlx5e-en_rep-Create-uplink-rep-root-table.patch
Patch239:	0240-netdrv-net-mlx5-E-Switch-Introduce-global-tables.patch
Patch240:	0241-netdrv-net-mlx5-E-Switch-Add-support-for-offloading-.patch
Patch241:	0242-netdrv-net-mlx5-E-Switch-Support-getting-chain-mappi.patch
Patch242:	0243-netdrv-net-mlx5e-CT-Introduce-connection-tracking.patch
Patch243:	0244-netdrv-net-mlx5e-CT-Offload-established-flows.patch
Patch244:	0245-netdrv-net-mlx5e-CT-Handle-misses-after-executing-CT.patch
Patch245:	0246-netdrv-net-mlx5e-CT-Support-clear-action.patch
Patch246:	0247-netdrv-net-mlx5e-CT-Fix-stack-usage-compiler-warning.patch
Patch247:	0248-netdrv-net-mlx5e-CT-Use-rhashtable-s-ct-entries-inst.patch
Patch248:	0249-netdrv-net-mlx5-CT-Change-idr-to-xarray-to-protect-p.patch
Patch249:	0250-netdrv-net-mlx5-E-switch-Fix-mutex-init-order.patch
Patch250:	0251-netdrv-net-mlx5-E-Switch-free-flow_group_in-after-cr.patch
Patch251:	0252-netdrv-net-mlx5-E-Switch-Enable-restore-table-only-i.patch
Patch252:	0253-netdrv-net-mlx5-Add-missing-inline-to-stub-esw_add_r.patch
Patch253:	0254-netdrv-net-mlx5-E-Switch-Fix-using-fwd-and-modify-wh.patch
Patch254:	0255-netdrv-net-mlx5e-Fix-rejecting-all-egress-rules-not-.patch
Patch255:	0256-netdrv-net-mlx5-E-switch-Fix-printing-wrong-error-va.patch
Patch256:	0257-netdrv-net-mlx5-E-Switch-Use-correct-type-for-chain-.patch
Patch257:	0258-netdrv-net-mlx5e-CT-Avoid-false-warning-about-rule-m.patch
Patch258:	0259-netdrv-net-mlx5e-Fix-actions_match_supported-return.patch
Patch259:	0260-netdrv-net-mlx5e-CT-Fix-insert-rules-when-TC_CT-conf.patch
Patch260:	0261-netdrv-net-mlx5e-CT-remove-set-but-not-used-variable.patch
Patch261:	0262-netdrv-net-mlx5e-Fix-missing-pedit-action-after-ct-c.patch
Patch262:	0263-netdrv-net-mlx5e-CT-Fix-offload-with-CT-action-after.patch
Patch263:	0264-netdrv-net-mlx5-E-switch-Annotate-termtbl_mutex-mute.patch
Patch264:	0265-netdrv-net-mlx5-E-switch-Annotate-esw-state_lock-mut.patch
Patch265:	0266-netdrv-net-mlx5-Avoid-deriving-mlx5_core_dev-second-.patch
Patch266:	0267-netdrv-net-mlx5-Simplify-mlx5_register_device-to-ret.patch
Patch267:	0268-netdrv-net-mlx5-Simplify-mlx5_unload_one-and-its-cal.patch
Patch268:	0269-netdrv-net-mlx5-Split-eswitch-mode-check-to-differen.patch
Patch269:	0270-netdrv-net-mlx5-E-switch-Extend-eswitch-enable-to-ha.patch
Patch270:	0271-netdrv-net-mlx5-E-switch-Protect-eswitch-mode-change.patch
Patch271:	0272-netdrv-net-mlx5e-Rename-representor-get-devlink-port.patch
Patch272:	0273-netdrv-net-mlx5e-Add-support-for-devlink-port-in-non.patch
Patch273:	0274-netdrv-net-mlx5e-Use-devlink-virtual-flavour-for-VF-.patch
Patch274:	0275-netdrv-net-mlx5e-Fix-devlink-port-register-sequence.patch
Patch275:	0276-netdrv-net-mlx5e-Fix-devlink-port-netdev-unregistrat.patch
Patch276:	0277-netdrv-net-mlx5-Fix-crash-upon-suspend-resume.patch
Patch277:	0278-netdrv-net-mlx5-Add-command-entry-handling-completio.patch
Patch278:	0279-netdrv-net-mlx5-Fix-a-race-when-moving-command-inter.patch
Patch279:	0280-netdrv-net-mlx5-Avoid-processing-commands-before-cmd.patch
Patch280:	0281-netdrv-net-mlx5e-Fix-allowed-tc-redirect-merged-eswi.patch
Patch281:	0282-netdrv-net-mlx5e-kTLS-Destroy-key-object-after-destr.patch
Patch282:	0283-netdrv-net-mlx5e-Fix-inner-tirs-handling.patch
Patch283:	0284-netdrv-net-mlx5-Fix-memory-leak-in-mlx5_events_init.patch
Patch284:	0285-netdrv-net-mlx5-Fix-cleaning-unmanaged-flow-tables.patch
Patch285:	0286-netdrv-net-mlx5-Don-t-maintain-a-case-of-del_sw_func.patch
Patch286:	0287-netdrv-net-mlx5-Annotate-mutex-destroy-for-root-ns.patch
Patch287:	0288-netdrv-net-mlx5e-Update-netdev-txq-on-completions-du.patch
Patch288:	0289-netdrv-net-mlx5e-CT-Correctly-get-flow-rule.patch
Patch289:	0290-netdrv-net-mlx5-Fix-error-flow-in-case-of-function_s.patch
Patch290:	0291-netdrv-net-mlx5e-IPoIB-Enable-loopback-packets-for-I.patch
Patch291:	0292-netdrv-net-mlx5e-IPoIB-Drop-multicast-packets-that-t.patch
Patch292:	0293-netdrv-net-mlx5-DR-Fix-incorrect-type-in-argument.patch
Patch293:	0294-netdrv-net-mlx5-DR-Fix-cast-to-restricted-__be32.patch
Patch294:	0295-netdrv-net-mlx5-DR-Fix-incorrect-type-in-return-expr.patch
Patch295:	0296-netdrv-net-mlx5-Accel-fpga-tls-fix-cast-to-__be64-an.patch
Patch296:	0297-netdrv-net-mlx5e-Allow-partial-data-mask-for-tunnel-.patch
Patch297:	0298-netdrv-net-mlx5e-en_tc-Fix-incorrect-type-in-initial.patch
Patch298:	0299-netdrv-net-mlx5e-en_tc-Fix-cast-to-restricted-__be32.patch
Patch299:	0300-netdrv-net-sched-expose-HW-stats-types-per-action-us.patch
Patch300:	0301-netdrv-net-mlx5e-Fix-stats-update-for-matchall-class.patch
Patch301:	0302-netdrv-net-mlx5e-Properly-set-default-values-when-di.patch
Patch302:	0303-netdrv-net-mlx5e-Fix-MLX5_TC_CT-dependencies.patch
Patch303:	0304-netdrv-net-mlx5e-replace-EINVAL-in-mlx5e_flower_pars.patch
Patch304:	0305-netdrv-net-mlx5e-Remove-warning-devices-are-not-on-s.patch
Patch305:	0306-include-net-mlx5-HW-bit-for-goto-chain-offload-suppo.patch
Patch306:	0307-include-netfilter-add-include-guard-to-xt_connlabel..patch
Patch307:	0308-include-netfilter-fix-include-guards.patch
Patch308:	0310-include-net-mlx5-IPSec-Fix-incorrect-type-for-spi.patch
Patch309:	0313-netdrv-net-mlx5e-Disable-devlink-port-support-for-no.patch
Patch310:	9001-Bump-driver-version.patch
Patch311:	9002-Add-mlx_backport_compat-h.patch
Patch312:	9003-Add-xsk_umem_adjust_offset.patch
Patch313:	9005-reporter_rx-strip-extack-parameter.patch
Patch314:	9006-Provide-DEVLINK_PORT_FLAVOUR_VIRTUAL-stub-value.patch
Patch315:	9007-Provide-TC_SETUP_FT-definition.patch
Patch316:	9008-Add-flow_action_basic_hw_stats_types_check
Patch317:	9009-add-NUM_FLOW_ACTIONS.patch

%define findpat %( echo "%""P" )
%define __find_requires /usr/lib/rpm/redhat/find-requires.ksyms
%define __find_provides /usr/lib/rpm/redhat/find-provides.ksyms %{kmod_name} %{?epoch:%{epoch}:}%{version}-%{release}
%define sbindir %( if [ -d "/sbin" -a \! -h "/sbin" ]; then echo "/sbin"; else echo %{_sbindir}; fi )
%define dup_state_dir %{_localstatedir}/lib/rpm-state/kmod-dups
%define kver_state_dir %{dup_state_dir}/kver
%define kver_state_file %{kver_state_dir}/%{kmod_kernel_version}.%(arch)
%define dup_module_list %{dup_state_dir}/rpm-kmod-%{kmod_name}-modules

Name:		kmod-redhat-mlx5_core
Version:	%{kmod_driver_version}
Release:	%{kmod_rpm_release}%{?dist}
%if "%{kmod_driver_epoch}" != ""
Epoch:		%{kmod_driver_epoch}
%endif
Summary:	mlx5_core kernel module for Driver Update Program
Group:		System/Kernel
License:	GPLv2
URL:		https://www.kernel.org/
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	%kernel_devel_pkg = %kmod_kernel_version
%if "%{kmod_dist_build_deps}" != ""
BuildRequires:	%{kmod_dist_build_deps}
%endif
ExclusiveArch:	x86_64
%global kernel_source() /usr/src/kernels/%{kmod_kernel_version}.$(arch)

%global _use_internal_dependency_generator 0
%if "%{?kmod_kernel_version_min}" != ""
Provides:	%kernel_modules_pkg >= %{kmod_kernel_version_min}.%{_target_cpu}
%else
Provides:	%kernel_modules_pkg = %{kmod_kernel_version_dep}.%{_target_cpu}
%endif
Provides:	kmod-%{kmod_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):	%{sbindir}/weak-modules
Requires(postun):	%{sbindir}/weak-modules
Requires:	kernel >= 4.18.0-193.el8

Requires:	kernel < 4.18.0-194.el8
%if 0
Requires: firmware(%{kmod_name}) = ENTER_FIRMWARE_VERSION
%endif
%if "%{kmod_build_dependencies}" != ""
BuildRequires:  %{kmod_build_dependencies}
%endif
%if "%{kmod_dependencies}" != ""
Requires:       %{kmod_dependencies}
%endif
# if there are multiple kmods for the same driver from different vendors,
# they should conflict with each other.
Conflicts:	kmod-%{kmod_name}

%description
mlx5_core kernel module for Driver Update Program

%if 0

%package -n kmod-redhat-mlx5_core-firmware
Version:	ENTER_FIRMWARE_VERSION
Summary:	mlx5_core firmware for Driver Update Program
Provides:	firmware(%{kmod_name}) = ENTER_FIRMWARE_VERSION
%if "%{kmod_kernel_version_min}" != ""
Provides:	%kernel_modules_pkg >= %{kmod_kernel_version_min}.%{_target_cpu}
%else
Provides:	%kernel_modules_pkg = %{kmod_kernel_version_dep}.%{_target_cpu}
%endif
%description -n  kmod-redhat-mlx5_core-firmware
mlx5_core firmware for Driver Update Program


%files -n kmod-redhat-mlx5_core-firmware
%defattr(644,root,root,755)
%{FIRMWARE_FILES}

%endif

# Development package
%if 0%{kmod_devel_package}
%package -n kmod-redhat-mlx5_core-devel
Version:	%{kmod_driver_version}
Requires:	kernel >= 4.18.0-193.el8

Requires:	kernel < 4.18.0-194.el8
Summary:	mlx5_core development files for Driver Update Program

%description -n  kmod-redhat-mlx5_core-devel
mlx5_core development files for Driver Update Program


%files -n kmod-redhat-mlx5_core-devel
%defattr(644,root,root,755)
/lib/modules/%{kmod_rpm_name}-%{kmod_driver_version}/
%endif

%post
modules=( $(find /lib/modules/%{kmod_kernel_version}.%(arch)/%{kmod_install_path} | grep '\.ko$') )
printf '%s\n' "${modules[@]}" | %{sbindir}/weak-modules --add-modules --no-initramfs

mkdir -p "%{kver_state_dir}"
touch "%{kver_state_file}"

exit 0

%posttrans
# We have to re-implement part of weak-modules here because it doesn't allow
# calling initramfs regeneration separately
if [ -f "%{kver_state_file}" ]; then
	kver_base="%{kmod_kernel_version_dep}"
	kvers=$(ls -d "/lib/modules/${kver_base%%.*}"*)

	for k_dir in $kvers; do
		k="${k_dir#/lib/modules/}"

		tmp_initramfs="/boot/initramfs-$k.tmp"
		dst_initramfs="/boot/initramfs-$k.img"

		# The same check as in weak-modules: we assume that the kernel present
		# if the symvers file exists.
		if [ -e "/boot/symvers-$k.gz" ]; then
			/usr/bin/dracut -f "$tmp_initramfs" "$k" || exit 1
			cmp -s "$tmp_initramfs" "$dst_initramfs"
			if [ "$?" = 1 ]; then
				mv "$tmp_initramfs" "$dst_initramfs"
			else
				rm -f "$tmp_initramfs"
			fi
		fi
	done

	rm -f "%{kver_state_file}"
	rmdir "%{kver_state_dir}" 2> /dev/null
fi

rmdir "%{dup_state_dir}" 2> /dev/null

exit 0

%preun
if rpm -q --filetriggers kmod 2> /dev/null| grep -q "Trigger for weak-modules call on kmod removal"; then
	mkdir -p "%{kver_state_dir}"
	touch "%{kver_state_file}"
fi

mkdir -p "%{dup_state_dir}"
rpm -ql kmod-redhat-mlx5_core-%{kmod_driver_version}-%{kmod_rpm_release}%{?dist}.$(arch) | \
	grep '\.ko$' > "%{dup_module_list}"

%postun
if rpm -q --filetriggers kmod 2> /dev/null| grep -q "Trigger for weak-modules call on kmod removal"; then
	initramfs_opt="--no-initramfs"
else
	initramfs_opt=""
fi

modules=( $(cat "%{dup_module_list}") )
rm -f "%{dup_module_list}"
printf '%s\n' "${modules[@]}" | %{sbindir}/weak-modules --remove-modules $initramfs_opt

rmdir "%{dup_state_dir}" 2> /dev/null

exit 0

%files
%defattr(644,root,root,755)
/lib/modules/%{kmod_kernel_version}.%(arch)
/etc/depmod.d/%{kmod_name}.conf
%doc /usr/share/doc/%{kmod_rpm_name}/greylist.txt



%prep
%setup -n %{kmod_name}-%{kmod_vendor}-%{kmod_driver_version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p1
%patch140 -p1
%patch141 -p1
%patch142 -p1
%patch143 -p1
%patch144 -p1
%patch145 -p1
%patch146 -p1
%patch147 -p1
%patch148 -p1
%patch149 -p1
%patch150 -p1
%patch151 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch155 -p1
%patch156 -p1
%patch157 -p1
%patch158 -p1
%patch159 -p1
%patch160 -p1
%patch161 -p1
%patch162 -p1
%patch163 -p1
%patch164 -p1
%patch165 -p1
%patch166 -p1
%patch167 -p1
%patch168 -p1
%patch169 -p1
%patch170 -p1
%patch171 -p1
%patch172 -p1
%patch173 -p1
%patch174 -p1
%patch175 -p1
%patch176 -p1
%patch177 -p1
%patch178 -p1
%patch179 -p1
%patch180 -p1
%patch181 -p1
%patch182 -p1
%patch183 -p1
%patch184 -p1
%patch185 -p1
%patch186 -p1
%patch187 -p1
%patch188 -p1
%patch189 -p1
%patch190 -p1
%patch191 -p1
%patch192 -p1
%patch193 -p1
%patch194 -p1
%patch195 -p1
%patch196 -p1
%patch197 -p1
%patch198 -p1
%patch199 -p1
%patch200 -p1
%patch201 -p1
%patch202 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1
%patch206 -p1
%patch207 -p1
%patch208 -p1
%patch209 -p1
%patch210 -p1
%patch211 -p1
%patch212 -p1
%patch213 -p1
%patch214 -p1
%patch215 -p1
%patch216 -p1
%patch217 -p1
%patch218 -p1
%patch219 -p1
%patch220 -p1
%patch221 -p1
%patch222 -p1
%patch223 -p1
%patch224 -p1
%patch225 -p1
%patch226 -p1
%patch227 -p1
%patch228 -p1
%patch229 -p1
%patch230 -p1
%patch231 -p1
%patch232 -p1
%patch233 -p1
%patch234 -p1
%patch235 -p1
%patch236 -p1
%patch237 -p1
%patch238 -p1
%patch239 -p1
%patch240 -p1
%patch241 -p1
%patch242 -p1
%patch243 -p1
%patch244 -p1
%patch245 -p1
%patch246 -p1
%patch247 -p1
%patch248 -p1
%patch249 -p1
%patch250 -p1
%patch251 -p1
%patch252 -p1
%patch253 -p1
%patch254 -p1
%patch255 -p1
%patch256 -p1
%patch257 -p1
%patch258 -p1
%patch259 -p1
%patch260 -p1
%patch261 -p1
%patch262 -p1
%patch263 -p1
%patch264 -p1
%patch265 -p1
%patch266 -p1
%patch267 -p1
%patch268 -p1
%patch269 -p1
%patch270 -p1
%patch271 -p1
%patch272 -p1
%patch273 -p1
%patch274 -p1
%patch275 -p1
%patch276 -p1
%patch277 -p1
%patch278 -p1
%patch279 -p1
%patch280 -p1
%patch281 -p1
%patch282 -p1
%patch283 -p1
%patch284 -p1
%patch285 -p1
%patch286 -p1
%patch287 -p1
%patch288 -p1
%patch289 -p1
%patch290 -p1
%patch291 -p1
%patch292 -p1
%patch293 -p1
%patch294 -p1
%patch295 -p1
%patch296 -p1
%patch297 -p1
%patch298 -p1
%patch299 -p1
%patch300 -p1
%patch301 -p1
%patch302 -p1
%patch303 -p1
%patch304 -p1
%patch305 -p1
%patch306 -p1
%patch307 -p1
%patch308 -p1
%patch309 -p1
%patch310 -p1
%patch311 -p1
%patch312 -p1
%patch313 -p1
%patch314 -p1
%patch315 -p1
%patch316 -p1
%patch317 -p1
set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
rm -rf obj
cp -r source obj

PWD_PATH="$PWD"
%if "%{workaround_no_pwd_rel_path}" != "1"
PWD_PATH=$(realpath --relative-to="%{kernel_source}" . 2>/dev/null || echo "$PWD")
%endif
%{make_build} -C %{kernel_source} V=1 M="$PWD_PATH/obj/%{kmod_kbuild_dir}" \
	NOSTDINC_FLAGS="-I$PWD_PATH/obj/include -I$PWD_PATH/obj/include/uapi %{nil}" \
	EXTRA_CFLAGS="%{nil}" \
	%{nil}
# mark modules executable so that strip-to-file can strip them
find obj/%{kmod_kbuild_dir} -name "*.ko" -type f -exec chmod u+x '{}' +

whitelist="/lib/modules/kabi-current/kabi_whitelist_%{_target_cpu}"
for modules in $( find obj/%{kmod_kbuild_dir} -name "*.ko" -type f -printf "%{findpat}\n" | sed 's|\.ko$||' | sort -u ) ; do
	# update depmod.conf
	module_weak_path=$(echo "$modules" | sed 's/[\/]*[^\/]*$//')
	if [ -z "$module_weak_path" ]; then
		module_weak_path=%{name}
	else
		module_weak_path=%{name}/$module_weak_path
	fi
	echo "override $(echo $modules | sed 's/.*\///')" \
	     "$(echo "%{kmod_kernel_version_dep}" |
	        sed 's/\.[^\.]*$//;
		     s/\([.+?^$\/\\|()\[]\|\]\)/\\\0/g').*" \
		     "weak-updates/$module_weak_path" >> source/depmod.conf

	# update greylist
	nm -u obj/%{kmod_kbuild_dir}/$modules.ko | sed 's/.*U //' |  sed 's/^\.//' | sort -u | while read -r symbol; do
		grep -q "^\s*$symbol\$" $whitelist || echo "$symbol" >> source/greylist
	done
done
sort -u source/greylist | uniq > source/greylist.txt

%install
export INSTALL_MOD_PATH=$RPM_BUILD_ROOT
export INSTALL_MOD_DIR=%{kmod_install_path}
PWD_PATH="$PWD"
%if "%{workaround_no_pwd_rel_path}" != "1"
PWD_PATH=$(realpath --relative-to="%{kernel_source}" . 2>/dev/null || echo "$PWD")
%endif
make -C %{kernel_source} modules_install \
	M=$PWD_PATH/obj/%{kmod_kbuild_dir}
# Cleanup unnecessary kernel-generated module dependency files.
find $INSTALL_MOD_PATH/lib/modules -iname 'modules.*' -exec rm {} \;

install -m 644 -D source/depmod.conf $RPM_BUILD_ROOT/etc/depmod.d/%{kmod_name}.conf
install -m 644 -D source/greylist.txt $RPM_BUILD_ROOT/usr/share/doc/%{kmod_rpm_name}/greylist.txt
%if 0
%{FIRMWARE_FILES_INSTALL}
%endif
%if 0%{kmod_devel_package}
install -m 644 -D $PWD/obj/%{kmod_kbuild_dir}/Module.symvers $RPM_BUILD_ROOT/lib/modules/%{kmod_rpm_name}-%{kmod_driver_version}/build/Module.symvers

if [ -n "%{kmod_devel_src_paths}" ]; then
	for i in %{kmod_devel_src_paths}; do
		mkdir -p "$RPM_BUILD_ROOT/lib/modules/%{kmod_rpm_name}-%{kmod_driver_version}/build/$(dirname "$i")"
		cp -rv "$PWD/source/$i" \
			"$RPM_BUILD_ROOT/lib/modules/%{kmod_rpm_name}-%{kmod_driver_version}/build/$i"
	done
fi
%endif



%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Oct 21 2020 Eugene Syromiatnikov <esyr@redhat.com> 5.0_0_dup8.2-2
- Bump release due to "Package build kmod-redhat-mlx5_core-5.0_0_dup8.2-1.el8_2
  kept gated because not onboarded to gating".

* Wed Oct 21 2020 Eugene Syromiatnikov <esyr@redhat.com> 5.0_0_dup8.2-1
- 86de78c2e6f431762836a4ea5891f891bc0fdcb4
- mlx5_core kernel module for Driver Update Program
- Resolves: #bz1889733
